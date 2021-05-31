import time
import numpy as np
import csv
import math
from pywinauto.application import Application
import pywinauto
import pandas as pd
import os

np.random.seed(1)


class Env:
    def __init__(self):
        super(Env, self).__init__()
        self.action_space = ['NG', 'G',]
        self.action_size = len(self.action_space)
        self.episode = 0
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

        # 0,0,0,0 으로 리셋
        s_ = [{'X': 0, 'Y': 0, 'Z': 0, 'G': 0}]
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_weightop.csv"
        field = ['X', 'Y', 'Z', 'G']
        with open(csv_dir, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writeheader()
            writer.writerows(s_)

        # 이전 stress, weight 리셋
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_compare.csv"
        with open(csv_dir, 'w', newline='') as f:
            reader = csv.writer(f)
            reader.writerow([0, 0])

        return self.get_state()

    def step(self, action):
        self.counter += 1

        # state를 받아옴
        state = self.get_state()

        # 액션에 따라 움직임
        self.move(state, action)

        # 완료여부, 리워드 설정
        if self.counter >= 64:
            done = True
            reward = self.simlab()
        else:
            done = False
            reward = 0
        # reward = self.set_reward(state)

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
        self.dig.set_focus()
        pywinauto.keyboard.send_keys("{VK_SHIFT down}S""{VK_SHIFT up}")

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
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_weightop.csv"
        field = ['X', 'Y', 'Z', 'G']
        with open(csv_dir, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=field)
            writer.writeheader()
            writer.writerows(s_)

    def get_state(self):
        # csv 파일 받아오기_state
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_weightop.csv"
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

    def simlab(self):
        # 심랩을 백그라운드에서 실행
        self.episode += 1
        print("백그라운드SimLab 실행중...{}".format(self.episode))
        simlab_dir = "\"C:\Program Files\Altair\\2021\SimLab2021\\bin\win64\SimLab.bat\""
        simscript_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Simlab_workingdir\simlab_test.py"
        os.system(simlab_dir + ' -auto ' + simscript_dir + ' -nographics')

        # CAE결과를 받아온다 / 무게, 응력
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\demo_simlabstress.csv"
        with open(csv_dir, 'r') as f:
            reader = csv.DictReader(f)
            dict_list = []
            for elemt in reader:
                dict_list.append(elemt)
        stress = float(dict_list[0][' value'])

        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\demo_simlabweight.csv"
        with open(csv_dir, 'r') as f:
            reader = csv.DictReader(f)
            dict_list = []
            for elemt in reader:
                dict_list.append(elemt)
        weight = float(dict_list[2][None][5][:12])*9.81

        # 이전값과 비교
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_compare.csv"
        with open(csv_dir, 'r') as f:
            reader = csv.reader(f)
            dict_list = []
            for elemt in reader:
                dict_list.append(elemt)
        pre_stress = float(dict_list[0][0])
        pre_weight = float(dict_list[0][1])
        reward = -1
        if pre_stress > stress:
            reward += 1
        if pre_weight > weight:
            reward += 1

        # csv 파일 작성하기_새로운 stress, weight에 대한
        csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_compare.csv"
        with open(csv_dir, 'w', newline='') as f:
            reader = csv.writer(f)
            reader.writerow([stress, weight])

        return reward
