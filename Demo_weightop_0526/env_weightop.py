import time
import numpy as np
import csv
import math
import fusion360_weightop
from pywinauto.application import Application
import pywinauto
import pandas as pd

np.random.seed(1)


class Env:
    def __init__(self):
        super(Env, self).__init__()
        self.action_space = ['NG', 'G',]
        self.action_size = len(self.action_space)

        self.counter = 0

        # 실행중 프로세스 받아오기
        procs = pywinauto.findwindows.find_elements()

        # 실행 중 프로세스에서 fusion360 찾기
        for proc in procs:
            if proc.name == 'Autodesk Fusion 360 (Personal - Not for Commercial Use)':
                print("찾았다!")
                break

        # 프로세스로 fusion360 연결
        app = Application(backend="uia").connect(process=proc.process_id)

        # dialog 연결
        self.dig = app['{}'.format(proc.name)]


    def set_reward(self, state):
        # state정의는 Simlab연결 후 정의, 리워드도
        state = [int(state[0]), int(state[1]), int(state[2]), int(state[3])]
        x = int(state[0])
        y = int(state[1])
        z = int(state[2])
        G = int(state[3])

        # 리워드 생성 (무게중심과 원점이 멀수록 -, 생성위치거리가 2보다 작으면 -)
        reward = 1

        return reward

    def reset(self):
        self.counter = 0

        # 0,0,0,0 으로 리셋
        s_ = [{'X': 0, 'Y': 0, 'Z': 0, 'G': 0}]
        csv_dir = r"C:\Users\break\Downloads\RLOptistruct\Demo\Demo_weightop_0526\Demo_weightop.csv"
        field = ['X', 'Y', 'Z', 'G']
        with open(csv_dir, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writeheader()
            writer.writerows(s_)

        return self.get_state()

    def step(self, action):
        self.counter += 1

        # state를 받아옴
        state = self.get_state()

        # 액션에 따라 움직임
        self.move(state, action)

        # 완료여부, 리워드 설정
        if self.counter > 64:
            done = True
        else:
            done = False
        reward = self.set_reward(state)

        s_ = self.get_state()

        return s_, reward, done

    def move(self, state, action):
        # 액션에 따라 생성 할지 안할지 결정
        state[3] = action
        # if action == 0:  # +x
        #     state[3] = 0
        # elif action == 1:  # -x
        #     state[3] = 1

        # fusion360 모델 생성
        fusion360_weightop.makeblock(self.dig)

        # 생성 위치 이동
        if self.counter % 16 == 0:
            state[0] = 0
            state[1] = 0
            state[2] += 1
        elif self.counter % 4 == 0:
                state[0] = 0
                state[1] += 1
        else:
            state[0] += 1

        s_ = [{'X': state[0], 'Y': state[1], 'Z': state[2], 'G':state[3]}]

        # csv 파일 작성하기_새로운 액션에 대한
        csv_dir = r"C:\Users\break\Downloads\RLOptistruct\Demo\Demo_weightop_0526\Demo_weightop.csv"
        field = ['X', 'Y', 'Z', 'G']
        with open(csv_dir, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writeheader()
            writer.writerows(s_)

    def get_state(self):
        # csv 파일 받아오기_state
        csv_dir = r"C:\Users\break\Downloads\RLOptistruct\Demo\Demo_weightop_0526\Demo_weightop.csv"
        with open(csv_dir, 'r') as f:
            reader = csv.DictReader(f)
            dict_list = []
            for elemt in reader:
                dict_list.append(elemt)
        if dict_list == []:
            print("빈 리스트")
        # # csv 파일 받아오기_state_pandas
        # csv_dir = r"C:\Users\break\Downloads\Fusion360_script\Demo\demo_com_0514\demo_com.csv"
        # data = pd.read_csv(csv_dir)

        X = int(dict_list[0]['X'])
        Y = int(dict_list[0]['Y'])
        Z = int(dict_list[0]['Z'])
        G = int(dict_list[0]['G'])

        # state설정
        state = [X, Y, Z, G]

        return state

