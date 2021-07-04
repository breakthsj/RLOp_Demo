# 실제로 Agent에서 실행되는 파일은 C:\Program Files\Altair\2021\SimLab2021\unity\bin\win64 에 있음
from hwx import simlab
#import simlab
import Generator_210630

import numpy as np
import csv
import os

# 디버그용 메시지
simlab.messageBox.popupmsg("작동 이상 없음_from Env")


class Env:
    def __init__(self):
        super(Env, self).__init__()
        self.action_space = ['NG', 'G']
        self.action_size = len(self.action_space)
        self.episode = 0
        self.counter = 0
        self.cell_cnt = 0
        self.SET = 1
        self.minweight = 0

        # 0620 state modified / real state : generated cor
        self.realstate = np.zeros(27)
        self.gcord = [0, 0, 0, 0]

    # def set_reward(self, state):
    #     # state정의는 Simlab연결 후 정의, 리워드도
    #     state = [int(state[0]), int(state[1]), int(state[2]), int(state[3])]
    #     x = int(state[0])
    #     y = int(state[1])
    #     z = int(state[2])
    #     G = int(state[3])
    #
    #     return reward

    def reset(self):
        self.counter = 0
        self.cell_cnt = 0

        # 0620 state modified / real state : generated cor
        self.realstate = np.zeros(27)
        self.gcord = [-15, -15, 5, 0]

        Generator_210630.init()
        Generator_210630.plate()

        return self.realstate

    def step(self, action):
        self.counter += 1

        # 액션에 따라 움직임 / modified state 0620
        self.move(action)

        # 완료여부(3 x 3 x 3), 리워드 설정
        if self.counter >= 27:
            done = True
            reward = self.simlab()
        else:
            done = False
            reward = 0
        # reward = self.set_reward(state)

        # # 0620 state modified / real state : generated cor
        s_ = self.realstate

        return s_, reward, done

    def move(self, action):
        # 디버그용
        # simlab.messageBox.popupmsg("counter : {}\ngcord : ".format(self.counter, self.gcord[3]))
        # 액션에 따라 생성 할지 안할지 결정
        self.gcord[3] = action

        # 생성 명령시
        if action:
            # 셀카운터 + 1
            self.cell_cnt += 1
            # SimLab 내부 생성
            Generator_210630.unitcell(self.gcord[0], self.gcord[1], self.gcord[2], self.cell_cnt)
            # state 바뀜
            self.realstate[(self.counter-1)] = 1

        # 생성 위치 이동
        if self.counter % 9 == 0:
            self.gcord[0] = -15
            self.gcord[1] = -15
            self.gcord[2] += 10
        elif self.counter % 3 == 0:
            self.gcord[0] = -15
            self.gcord[1] += 10
        else:
            self.gcord[0] += 10

    def simlab(self):
        # 심랩을 백그라운드에서 실행
        self.episode += 1
        # print("백그라운드SimLab 실행중...{}".format(self.episode))
        # simlab_dir = "\"C:\Program Files\Altair\\2021\SimLab2021\\bin\win64\SimLab.bat\""
        # simscript_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Simlab_workingdir_modi\simlab_moditest.py"
        # os.system(simlab_dir + ' -auto ' + simscript_dir + ' -nographics')
        # # os.system(simlab_dir + ' -auto ' + simscript_dir)

        Generator_210630.solve()

        # CAE결과를 받아온다 / 무게, 응력
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\210629_MultilayerDemo\SimLab_response.csv"
        with open(csv_dir, 'r') as f:
            reader = csv.reader(f)
            dict_list = []
            for elemt in reader:
                dict_list.append(elemt)
        stress = float(dict_list[1][1])

        if stress <= 40:
            reward = 1
        else:
            reward = -1

        # # 최소 무게 설정
        # if self.SET:
        #     if stress <= 40:
        #         self.minweight = weight
        #         self.SET = 0
        #
        # # 리워드 설정
        # reward = 0
        # if weight == 0:
        #     reward = -10
        # elif stress <= 40:
        #     reward = 5
        #     if self.minweight >= weight:
        #         reward += 10
        #         self.minweight = weight
        #         os.replace(r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_Simlab_result.slb",
        #                    r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_Simlab_optishape.slb")
        #     elif self.minweight*1.3 >= weight:
        #         reward += 8
        #     elif self.minweight*1.6 >= weight:
        #         reward += 6
        #     elif self.minweight*2.0 >= weight:
        #         reward += 4
        #     elif self.minweight*2.5 <= weight:
        #         reward -= 4
        #     elif self.minweight*3.0 <= weight:
        #         reward -= 8
        # else:
        #     reward = -10
        #
        # #현재 상태 출력
        # print("모델 응력 : {:.3f}Mpa | 모델 무게 : {:.3f}kg | 현재 무게 최저치 : {:.3f}kg".format(stress, weight, self.minweight))
        #
        # # csv 파일 작성하기_새로운 stress, weight에 대한
        # csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_compare.csv"
        # with open(csv_dir, 'w', newline='') as f:
        #     reader = csv.writer(f)
        #     reader.writerow([stress, weight])

        return reward
