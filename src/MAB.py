import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import init_data_file as idf


exploration_rate = 0.1
sigma = 0.1
# real_reward = [0.1,0.3,0.2,0.5,0.1]

def random_select(N,real_reward,k):
    expect_reward_estimate = [0]*k
    operation = [0]*k
    total_reward = 0
    for i in range(N):
        arm = np.random.choice(k , size=1)[0]
        arm_reward = np.random.binomial(1 , real_reward[arm] , size=1)[0]

        expect_reward_estimate[arm] = (expect_reward_estimate[arm]*operation[arm] + arm_reward)/(operation[arm] + 1)

        operation[arm] += 1

        total_reward += arm_reward
    return total_reward,expect_reward_estimate,operation

def boltzman(N , sigma,real_reward,k):
    expect_reward_estimate = [0]*k
    operation = [0]*k
    total_reward = 0
    for i in range(N):
        reward_prob = np.exp(np.array(expect_reward_estimate)/sigma)/np.exp(np.array(expect_reward_estimate)/sigma).sum()
        best_arm = np.random.choice(k , size=1 , p=reward_prob)[0]
        best_arm_reward = np.random.binomial(1 , real_reward[best_arm] , size=1)[0]

        expect_reward_estimate[best_arm] = (expect_reward_estimate[best_arm] * operation[best_arm] + best_arm_reward)/(operation[best_arm] + 1)
        operation[best_arm] += 1
        total_reward += best_arm_reward
    return total_reward, expect_reward_estimate, operation

def ucb(N,real_reward,k):
    expect_reward_estimate = [0]*k
    operation = [0]*k
    total_reward = 0
    for i in range(N):
        max_upper_bound = 0

        for j in range(k):
            if(operation[j] > 0):
                delta_i = np.sqrt(2*np.log(i+1)/operation[j])
                upper_bound = expect_reward_estimate[j] + delta_i
            else:
                upper_bound = 1e400
            if upper_bound > max_upper_bound:
                max_upper_bound = upper_bound
                best_arm = j
        best_arm_reward = np.random.binomial(1,real_reward[best_arm],size=1)[0]
        expect_reward_estimate[best_arm] = (expect_reward_estimate[best_arm]
                                            *operation[best_arm] +
                                            best_arm_reward)/(operation[best_arm]+1)
        operation[best_arm] += 1
        total_reward += best_arm_reward
    return total_reward,expect_reward_estimate,operation


def epsilon_greedy(N , exploration_rate,real_reward,k):
    expect_reward_estimate = [0]*k
    operation = [0]*k
    total_reward = 0

    for i in range(N):
        r = np.random.uniform(size=1)[0]
        if r > exploration_rate:
            best_arm = expect_reward_estimate.index(max(expect_reward_estimate))
        else:
            best_arm = np.random.choice(k , size =1)[0]
        best_arm_reward = np.random.binomial(1,real_reward[best_arm],size=1)[0]
        expect_reward_estimate[best_arm] = (expect_reward_estimate[best_arm] * operation[best_arm] + best_arm_reward)/(operation[best_arm] + 1)
        operation[best_arm]  += 1
        total_reward += best_arm_reward
    return total_reward, expect_reward_estimate, operation


#mab个人实现
def get_max(list_group):
    max_index = 0
    list_index = 0
    for num in list_group:
        if num > list_group[max_index]:
            max_index = list_index
        list_index += 1
    return max_index

class MAB:
    def __init__(self):
        self.q = []#记录每个动作获得的标签
        self.action_counts = 0#所有动作的次数
        self.q_num = []#记录每个标签各自的次数

    def e_greedy(self,list):
        epsilon = 0.2#参数
        # print('starting training..')
        action = 1
        self.q.append(list[0])
        self.q_num.append(1)
        for i in range(5000):
            if np.random.random() < epsilon:#利用
                max = get_max(self.q_num)
                self.q_num[max] += 1
            else:
                index = np.random.randint(0,20)#探索
                if list[index] in self.q:
                    for k in range(action):
                        if list[index] == self.q[k]:
                            self.q_num[k] += 1
                else:
                    self.q.append(list[index])
                    self.q_num.append(0)
                    action += 1
            self.action_counts += 1
        for i in range(action):
            self.q_num[i] = (float)(self.q_num[i]/self.action_counts)
        return self.q,self.q_num,action

def get_file():
        files_matrix = []
        file_data = idf.DataFile()
        vel,files = file_data.gen_file()
        movies = file_data.read_file()
        # print(movies)
        # print(files)
        for i in range(file_data.vechile_num):
            file_matrix = []
            for k in range(file_data.file_num):
                # print(files[i][k])
                # print(movies[files[i][k]][:])
                file_matrix.append(movies[files[0][k]][:])
            files_matrix.append(file_matrix)
        return files_matrix

        # files_matrix = []
        # file_data = idf.DataFile()
        # movies = file_data.read_file()
        # for i in range(file_data.file_num):
        #     file_matrix = []
        #     file_matrix.append(movies[:])


def select_mab_kind(text):
    print(text)
    files_matrix = []
    file_data = idf.DataFile()
    vel,files = file_data.gen_file()
    movies = file_data.read_file()
    for i in range(file_data.vechile_num):
        file_matrix = []
        for k in range(file_data.file_num):
            file_matrix.append(movies[files[i][k]][0:2])
        files_matrix.append(file_matrix)
        # print(file_matrix)
    example = MAB()
    # print(files_matrix[0])
    a,b,c = example.e_greedy(files_matrix[0])
    print(b)
    print(c)
    # total_reward = 0
    # for i in range(c):
    #     print("kind:{0} reward:{1}".format(a[i],b[i]))
    #     total_reward += b[i]
    # print('total_reward:',total_reward)



    n = 1000
    total_reward1, expect_reward1, operation_times1 = epsilon_greedy(n,0.1,b,c)
    total_reward2, expect_reward2, operation_times2 = ucb(n, b, c)
    total_reward3, expect_reward3, operation_times3 = boltzman(n, 0.1, b, c)
    print("随机选择的累积奖励：{0},{1},{2}".format(total_reward1,total_reward2,total_reward3))
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # 在0到1之间生成100个探索率
    explore_grad = np.arange(0.01, 1.01, 0.01)


    #在不同探索率下，ε-greedy策略的累积奖励
    reward_result = [epsilon_greedy(n, i, b,c)[0] for i in explore_grad]


    #绘制折线图
    if text == 'egreedy':
        plt.figure(figsize=(8, 6))
        plt.plot(explore_grad, reward_result, c='deepskyblue')
        plt.xlabel('探索率', fontsize=12)
        plt.ylabel('累积奖励', fontsize=12)
        plt.xlim(0, 1)
        plt.show()
    elif text == '三种策略奖励对比':
        reward = [total_reward1,total_reward2,total_reward3]
        explore = ['epsilon_greedy','ucb','boltzman']
        print(reward,explore)
        plt.figure()
        plt.bar(explore,reward,width=0.2)
        for x,y in zip(explore,reward):
            plt.text( x , y , '%.2f' % y, ha='center',va='bottom',fontsize=10)
        plt.xlabel('策略', fontsize=12)
        plt.ylabel('总奖励', fontsize=12)
        # plt.xlim(0, 1)
        plt.show()


    # expect_reward_table = pd.DataFrame({
    #     '期望奖励' : expect_reward,
    #     '操作次数' : operation_times
    # })
    # print(expect_reward_table)

if __name__ == '__main__':
    select_mab_kind(ucb)



