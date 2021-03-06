#***************************************************************
#SimLab Version 2021
#Created at Thu Jun 24 16:31:32 2021
#***************************************************************
#For debugging this python script,Please comment(#) out the line "from hwx import simlab" and uncomment the line "import simlab"
from hwx import simlab
# import simlab
import time
import os
import sys
import pylab
import random
import numpy as np
from collections import deque
import tensorflow as tf
import keras
from keras.layers import Dense, Input
from keras.optimizers import Adam
from keras.initializers import RandomUniform
from keras.models import Model

from Env_210630 import Env
import Generator_210630

# 디버그용 메시지
# simlab.messageBox.popupmsg("import 이상 없음_from Agent")
# print("start")


# gpu 상태 점검 / vram 50% 할당
# config = tf.compat.v1.ConfigProto()
# config.gpu_options.per_process_gpu_memory_fraction = 0.5
# session = tf.compat.v1.Session(config=config)
config = tf.ConfigProto()
config.gpu_options.per_process_gpu_memory_fraction = 0.5
session = tf.Session(config=config)



def build_network(state_size, action_size):
    state_input = Input((state_size,))
    h1 = Dense(32, activation='relu')(state_input)
    h2 = Dense(32, activation='relu')(h1)
    out = Dense(action_size, activation='relu')(h2)

    model = Model(state_input, out)

    return model


# 카트폴 예제에서의 DQN 에이전트
class DQNAgent:
    def __init__(self, state_size, action_size):
        self.render = False

        # 상태와 행동의 크기 정의
        self.state_size = state_size
        self.action_size = action_size

        # DQN 하이퍼파라미터
        self.discount_factor = 0.99
        self.learning_rate = 0.001
        self.epsilon = 1.0
        self.epsilon_decay = 0.9999
        self.epsilon_min = 0.01
        self.batch_size = 256
        self.train_start = 1000

        # 리플레이 메모리, 최대 크기 2000
        self.memory = deque(maxlen=2000)

        # 모델과 타깃 모델 생성
        self.model = build_network(self.state_size, self.action_size)
        self.target_model = build_network(self.state_size, self.action_size)
        self.optimizer = Adam(lr=self.learning_rate)

        # # Continue learning
        # self.model.load_weights("./save_model/trained/model")

        # 타깃 모델 초기화
        self.update_target_model()

    # 타깃 모델을 모델의 가중치로 업데이트
    def update_target_model(self):
        self.target_model.set_weights(self.model.get_weights())

    # 입실론 탐욕 정책으로 행동 선택
    def get_action(self, state):
        if np.random.rand() <= self.epsilon:
            return random.randrange(self.action_size)
        else:
            q_value = self.model(state)
            return np.argmax(q_value[0])

    # 샘플 <s, a, r, s'>을 리플레이 메모리에 저장
    def append_sample(self, state, action, reward, next_state, done):
        self.memory.append((state, action, reward, next_state, done))

    # 리플레이 메모리에서 무작위로 추출한 배치로 모델 학습
    def train_model(self):
        if self.epsilon > self.epsilon_min:
            self.epsilon *= self.epsilon_decay

        # 메모리에서 배치 크기만큼 무작위로 샘플 추출
        mini_batch = random.sample(self.memory, self.batch_size)

        states = np.array([sample[0][0] for sample in mini_batch])
        actions = np.array([sample[1] for sample in mini_batch])
        rewards = np.array([sample[2] for sample in mini_batch])
        next_states = np.array([sample[3][0] for sample in mini_batch])
        dones = np.array([sample[4] for sample in mini_batch])

        # 학습 파라메터
        try:
            model_params = self.model.trainable_variables
        except Exception as e:
            pass
            # simlab.messageBox.popupmsg("{}".format(e))

        with tf.GradientTape() as tape:
            # 현재 상태에 대한 모델의 큐함수
            predicts = self.model(states)
            one_hot_action = tf.one_hot(actions, self.action_size)
            predicts = tf.reduce_sum(one_hot_action * predicts, axis=1)

            # 다음 상태에 대한 타깃 모델의 큐함수
            target_predicts = self.target_model(next_states)
            target_predicts = tf.stop_gradient(target_predicts)

            # 벨만 최적 방정식을 이용한 업데이트 타깃
            max_q = np.amax(target_predicts, axis=-1)
            targets = rewards + (1 - dones) * self.discount_factor * max_q
            loss = tf.reduce_mean(tf.square(targets - predicts))
        # 오류함수를 줄이는 방향으로 모델 업데이트
        grads = tape.gradient(loss, model_params)
        self.optimizer.apply_gradients(zip(grads, model_params))


if __name__ == "__main__":
    try:
        # 환경과 에이전트 생성
        env = Env()
        state_size = 27
        action_space = [0, 1]
        action_size = len(action_space)

        agent = DQNAgent(state_size, action_size)
        scores, episodes = [], []
        score_avg = 0

        EPISODES = 1500
        for e in range(EPISODES):
            start_time = time.time()
            done = False
            score = 0
            # env 초기화
            state = env.reset()
            state = np.reshape(state, [1, state_size])

            while not done:
                # 현재 상태에 대한 행동 선택
                action = agent.get_action(state)

                # 선택한 행동으로 환경에서 한 타임스텝 진행 후 샘플 수집
                next_state, reward, done = env.step(action)
                next_state = np.reshape(next_state, [1, state_size])

                score += reward

                # 리플레이 메모리에 샘플 <s, a, r, s'> 저장
                agent.append_sample(state, action, reward, next_state, done)
                # 매 타임스텝마다 학습
                # if len(agent.memory) >= agent.train_start:
                #     agent.train_model()

                state = next_state

                if done:
                    # 에피소드마다 걸린 시간 측정
                    end_time = time.time()
                    spend_time = float(end_time-start_time)
                    # 각 에피소드마다 타깃 모델을 모델의 가중치로 업데이트
                    agent.update_target_model()
                    # 에피소드마다 학습 결과 출력
                    score_avg = 0.9 * score_avg + 0.1 * score if score_avg != 0 else score
                    # simlab.messageBox.popupmsg("episode: {:3d} | score avg: {:3.2f} | memory length: {:4d} | epsilon: {:.4f} | time(s): {:.3f}".format(
                    #     e, score_avg, len(agent.memory), agent.epsilon, spend_time))
                    simlab.printToLogFile("episode: {:3d} | score avg: {:3.2f} | memory length: {:4d} | epsilon: {:.4f} | time(s): {:.3f}".format(
                        e, score_avg, len(agent.memory), agent.epsilon, spend_time))

            #         # 에피소드마다 학습 결과 그래프로 저장
            #         scores.append(score_avg)
            #         episodes.append(e)
            #         pylab.plot(episodes, scores, 'b')
            #         pylab.xlabel("episode")
            #         pylab.ylabel("average score")
            #         pylab.savefig("./save_graph/graph.png")
            #
            # # 100 에피소드마다 모델 저장
            # if e % 100 == 0:
            #     agent.model.save_weights('save_model/model', save_format='tf')
    except Exception as e:
        # pass
        simlab.messageBox.popupmsg("{}".format(e))
        simlab.printToLogFile("{}".format(e))