import numpy as np
import csv
import os


class Env:
    def __init__(self):
        super(Env, self).__init__()
        self.action_space = ['NG', 'G']
        self.action_size = len(self.action_space)
        self.episode = 0
        self.counter = 0
        self.SET = 1
        self.minweight = 0

        # 0620 state modified / real state : generated cor
        self.realstate = np.zeros(25)
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

        # 0620 state modified / real state : generated cor
        self.realstate = np.zeros(25)
        self.gcord = [0, 0, 0, 0]

        return self.realstate

    def step(self, action):
        self.counter += 1

        # 액션에 따라 움직임 / modified state 0620
        # self.realstate = self.move(action)

        # 완료여부(3 x 3 x 1), 리워드 설정
        if self.counter >= 9:
            done = True
            # reward = self.simlab()
            reward = 1
        else:
            done = False
            reward = 0
        # reward = self.set_reward(state)

        # # 0620 state modified / real state : generated cor
        s_ = self.realstate

        return s_, reward, done

    def move(self, action):
        # 액션에 따라 생성 할지 안할지 결정
        self.gcord[3] = action

        # 생성 위치 이동
        # if self.counter % 16 == 0:
        #     state[0] = 0
        #     state[1] = 0
        #     state[2] += 1
        # elif self.counter % 4 == 0:
        #         state[0] = 0
        #         state[1] += 1
        if self.counter % 5 == 0:
            self.gcord[0] = 0
            self.gcord[1] += 1
        else:
            self.gcord[0] += 1

        # # 0620 state modified / real state : generated cor
        if action:
            self.realstate[(self.counter-1)] = 1

        return self.realstate

    # def get_state(self):
    #     # csv 파일 받아오기_state
    #     csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_weightop.csv"
    #     with open(csv_dir, 'r') as f:
    #         reader = csv.DictReader(f)
    #         dict_list = []
    #         for elemt in reader:
    #             dict_list.append(elemt)
    #     if dict_list == []:
    #         print("빈 리스트")
    #     # # csv 파일 받아오기_state_pandas
    #     # csv_dir = r"C:\Users\break\Downloads\Fusion360_script\Demo\demo_com_0514\demo_com.csv"
    #     # data = pd.read_csv(csv_dir)
    #
    #     X = int(dict_list[0]['X'])
    #     Y = int(dict_list[0]['Y'])
    #     Z = int(dict_list[0]['Z'])
    #     G = int(dict_list[0]['G'])
    #
    #     # state설정
    #     state = [X, Y, Z, G]
    #
    #     return state

    # def simlab(self):
    #     # 심랩을 백그라운드에서 실행
    #     self.episode += 1
    #     print("백그라운드SimLab 실행중...{}".format(self.episode))
    #     simlab_dir = "\"C:\Program Files\Altair\\2021\SimLab2021\\bin\win64\SimLab.bat\""
    #     simscript_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Simlab_workingdir_modi\simlab_moditest.py"
    #     os.system(simlab_dir + ' -auto ' + simscript_dir + ' -nographics')
    #     # os.system(simlab_dir + ' -auto ' + simscript_dir)
    #
    #     # CAE결과를 받아온다 / 무게, 응력
    #     csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\demo_simlabstress.csv"
    #     with open(csv_dir, 'r') as f:
    #         reader = csv.DictReader(f)
    #         dict_list = []
    #         for elemt in reader:
    #             dict_list.append(elemt)
    #     stress = float(dict_list[0][' value'])
    #
    #     csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\demo_simlabweight.csv"
    #     with open(csv_dir, 'r') as f:
    #         reader = csv.DictReader(f)
    #         dict_list = []
    #         for elemt in reader:
    #             dict_list.append(elemt)
    #     weight = float(dict_list[2][None][5][:12])*9.81
    #
    #     # 이전값과 비교
    #     csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_compare.csv"
    #     with open(csv_dir, 'r') as f:
    #         reader = csv.reader(f)
    #         dict_list = []
    #         for elemt in reader:
    #             dict_list.append(elemt)
    #     pre_stress = float(dict_list[0][0])
    #     pre_weight = float(dict_list[0][1])
    #
    #     # 최소 무게 설정
    #     if self.SET:
    #         if stress <= 40:
    #             self.minweight = weight
    #             self.SET = 0
    #
    #     # 리워드 설정
    #     reward = 0
    #     if weight == 0:
    #         reward = -10
    #     elif stress <= 40:
    #         reward = 5
    #         if self.minweight >= weight:
    #             reward += 10
    #             self.minweight = weight
    #             os.replace(r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_Simlab_result.slb",
    #                        r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_Simlab_optishape.slb")
    #         elif self.minweight*1.3 >= weight:
    #             reward += 8
    #         elif self.minweight*1.6 >= weight:
    #             reward += 6
    #         elif self.minweight*2.0 >= weight:
    #             reward += 4
    #         elif self.minweight*2.5 <= weight:
    #             reward -= 4
    #         elif self.minweight*3.0 <= weight:
    #             reward -= 8
    #     else:
    #         reward = -10
    #
    #     #현재 상태 출력
    #     print("모델 응력 : {:.3f}Mpa | 모델 무게 : {:.3f}kg | 현재 무게 최저치 : {:.3f}kg".format(stress, weight, self.minweight))
    #
    #     # csv 파일 작성하기_새로운 stress, weight에 대한
    #     csv_dir = r"C:\Users\break\Downloads\RLOp_Demo\Demo_weightop_0526\Demo_compare.csv"
    #     with open(csv_dir, 'w', newline='') as f:
    #         reader = csv.writer(f)
    #         reader.writerow([stress, weight])
    #
    #     return reward
