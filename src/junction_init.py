import numpy as np
# import q_learning as ql
import Global_Par as Gp
adj_martix = [[0 for i in range(80)] for i in range(80)]
junction_position = [[0 for i in range(2)] for i in range(80)]
junction_distance = [[0 for i in range(80)] for i in range(80)]
num_segement_martix = [[0 for i in range(4)] for i in range(80)]
veh_segement_martix = [[[] for i in range(4)] for i in range(80)]
junction_vehicle = [[0 for i in range(0)] for i in range(80)]
chosen_edge = [[0 for i in range(80)] for i in range(80)]
edge_list = []
e_arrival_time = [Gp.MAX for i in range(600)]
junction_dp_weight = [[0 for i in range(80)] for i in range(80)]
junction_greedy_weight = [[0 for i in range(80)] for i in range(80)]


def inti():
    for i in range(8):
        adj_martix[i * 10][i * 10 + 1] = 341.8
        junction_position[i * 10 + 1][0] = 341.8
        adj_martix[i * 10 + 1][i * 10 + 2] = 243.2
        junction_position[i * 10 + 2][0] = 585
        adj_martix[i * 10 + 2][i * 10 + 3] = 218.1
        junction_position[i * 10 + 3][0] = 803.1
        adj_martix[i * 10 + 3][i * 10 + 4] = 376
        junction_position[i * 10 + 4][0] = 1179.1
        adj_martix[i * 10 + 4][i * 10 + 5] = 215.6
        junction_position[i * 10 + 5][0] = 1394.7
        adj_martix[i * 10 + 5][i * 10 + 6] = 240.2
        junction_position[i * 10 + 6][0] = 1634.9
        adj_martix[i * 10 + 6][i * 10 + 7] = 326.2
        junction_position[i * 10 + 7][0] = 1961.1
        adj_martix[i * 10 + 7][i * 10 + 8] = 250.5
        junction_position[i * 10 + 8][0] = 2211.6
        adj_martix[i * 10 + 8][i * 10 + 9] = 347.6
        junction_position[i * 10 + 9][0] = 2559.2

    for i in range(10):
        adj_martix[i][10 + i] = 356.9
        junction_position[10 + i][1] = 356.9
        adj_martix[10 + i][20 + i] = 152
        junction_position[20 + i][1] = 508.9
        adj_martix[20 + i][30 + i] = 163
        junction_position[30 + i][1] = 671.9
        adj_martix[30 + i][40 + i] = 188.7
        junction_position[40 + i][1] = 860.6
        adj_martix[40 + i][50 + i] = 176.6
        junction_position[50 + i][1] = 1037.2
        adj_martix[50 + i][60 + i] = 247.5
        junction_position[60 + i][1] = 1284.7
        adj_martix[60 + i][70 + i] = 201
        junction_position[70 + i][1] = 1485.7


    for i in range(2, 9):
        junction_position[30 + i] = [-1, -1]
        adj_martix[20 + i][30 + i] = 0
        adj_martix[30 + i][40 + i] = 0
        adj_martix[20 + i][40 + i] = 351.7

    adj_martix[61][62] = 0
    junction_position[62] = [-1, -1]
    adj_martix[62][63] = 0
    adj_martix[61][63] = 461.3

    adj_martix[71][72] = 0
    junction_position[72] = [-1, -1]
    adj_martix[72][73] = 0
    adj_martix[71][73] = 461.3

    adj_martix[63][64] = 0
    junction_position[64] = [-1, -1]
    adj_martix[64][65] = 0
    adj_martix[63][65] = 591.6

    adj_martix[73][74] = 0
    junction_position[74] = [-1, -1]
    adj_martix[74][75] = 0
    adj_martix[73][75] = 591.6


    adj_martix[75][76] = 0
    junction_position[76] = [-1, -1]
    adj_martix[76][77] = 0
    adj_martix[75][77] = 566.4


    for i in range(80):
        for j in range(i):
            if (junction_position[i][0] >= 0 and junction_position[i][1] >= 0) and (junction_position[j][0] >= 0 and junction_position[j][1] >= 0):
                a = pow(pow(junction_position[i][0]-junction_position[j][0], 2)+pow(junction_position[i][1]-junction_position[j][1], 2), 0.5)
                junction_distance[i][j] = a
                junction_distance[j][i] = a

    qeq = np.transpose(adj_martix)
    for i in range(80):
        for j in range(80):
            if qeq[i][j] != 0:
                adj_martix[i][j] = qeq[i][j]


