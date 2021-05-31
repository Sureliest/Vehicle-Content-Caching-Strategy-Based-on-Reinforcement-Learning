import numpy as np
import re
# from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
# from matplotlib.figure import Figure
import matplotlib.pyplot as plt

import Init
import Global_Par as gp
import Server
import random
import math
import simulation as simu


# 获取车辆节点的数量和仿真时间
def get_sim_parameter(configfile_path):
    with open(configfile_path, 'r') as f:
        for line in f:
            if line.find('set opt(nn)') >= 0:
                line_list = re.split('[\s]', line)
                node_num = int(float(line_list[2]))
            if line.find('set opt(stop)') >= 0:
                line_list = re.split('[\s]', line)
                sim_time = int(float(line_list[2]))
    return node_num, sim_time


# 获取车量节点的初始位置以及运动轨迹的变化情况
def get_position(mobile_file_path):
    x_max = 0
    y_max = 0
    z_max = 0
    with open(mobile_file_path, 'r') as f:
        movement_list = []
        init_position_list = []
        item_list = []
        key = 0
        for line in f:
            line_list = re.split('[\s]', line)
            if line_list[0] != '':
                # 输出样例
                item_list.append(float(line_list[2]))  # 时间
                item_list.append(float(line_list[3][8:-1]))  # 结点编号
                if float(line_list[5]) > x_max:  # x,y是位置信息，z是速度信息
                    x_max = float(line_list[5])
                if float(line_list[6]) > y_max:
                    y_max = float(line_list[6])
                if float(line_list[7][0:-1]) > z_max:
                    z_max = float(line_list[7][0:-1])
                item_list.append(float(line_list[5]))
                item_list.append(float(line_list[6]))
                item_list.append(float(line_list[7][0:-1]))
                movement_list.append(item_list)
                item_list = []
            else:
                key = key + 1
                # 将节点编号写入列表
                if key % 3 == 1:
                    item_list.append(int(line_list[1][7:-1]))  # 结点编号
                # 将节点的位置(x,y)和z写入列表
                if key % 3 != 0:
                    item_list.append(float(line_list[4]))
                if key % 3 == 0:
                    item_list.append(float(line_list[4]))
                    init_position_list.append(item_list)
                    item_list = []
        # print("x:",x_max)
        # print("y:",y_max)
        # print("z",z_max)
        movement_matrix = np.mat(movement_list)  # 移动情况
        init_position_matrix = np.mat(init_position_list)  # 结点初始位置
        return movement_matrix, init_position_matrix, x_max, y_max


# node_position节点位置的变化情况，共有6个元素，包括时间，节点编号，当前x坐标，当前y坐标，目的位置x坐标，目的位置y坐标,节点移动速度
def update_node_position(movement_matrix, node_position, start_t, update_period, animation, nodelist, com_nodelist,
                         controller):
    print('开始时间:', start_t)
    active_route = []
    current_move = movement_matrix[np.nonzero(movement_matrix[:, 0].A == start_t)[0], :]
    # print('current_move:',current_move)
    for value in current_move:
        for i in range(2, 4):
            node_position[int(value[0, 1]), i + 2] = value[0, i]  # 更新结点的目标位置
    # print(node_position[0:5])
    # print('update_current_move[1]:',node_position[0:5])

    speed_x = node_position[:, 4] - node_position[:, 2]
    speed_y = node_position[:, 5] - node_position[:, 3]

    for i in range(0, int(1.0 / gp.update_period)):
        # 更新当前位置信息
        node_position[:, 2] = node_position[:, 2] + speed_x * gp.update_period
        node_position[:, 3] = node_position[:, 3] + speed_y * gp.update_period
        # 记录结点的位置信息
        node_id_position = node_position[:, [1, 2, 3]]

        if nodelist == [] and com_nodelist == []:
            nodelist.extend(Init.init_node(node_id_position, controller))
            com_nodelist.extend(Init.get_communication_node(node_id_position.shape[0]))

        print('{0} time,veichle context is training.....'.format(start_t))
        for node in nodelist:
            node.request_cache()

        # 进行仿真模拟
        simu.simulation(node_id_position, nodelist, com_nodelist, i, controller)

        if animation:
            plt.clf()
            plt.plot(node_position[:, 2], node_position[:, 3], '.m')
            # plt.scatter(([controller.rsus[i].position_x] for i in 500), ([controller.rsus[i].position_y] for i in 500), c = 'blue')
            plt.pause(update_period)  # 0.01


def control_movement(animation):
    print(animation)
    np.set_printoptions(suppress=True)
    config_file_path = r'grid.config.tcl'  # 可以读取节点数量和仿真时间
    mobile_file_path = r'tiexi.tcl'
    node_num, sim_time = get_sim_parameter(config_file_path)  # node_num节点数量,sim_time 时间
    movement_matrix, init_position_matrix, x_max, y_max = get_position(mobile_file_path)
    init_position_arranged = init_position_matrix[np.lexsort(init_position_matrix[:, ::-1].T)]  # 排序，mat会导致变为三维

    node_position = init_position_arranged[0]  # 二维

    node_position = np.insert(node_position, 0, values=np.zeros(node_num), axis=1)
    # print('node_position1:\n',node_position) 已经按照结点顺序 排序好的初始位置矩阵
    # print("node_position1:",node_position)

    node_position = np.column_stack((node_position, node_position[:, 2:4]))  # 按列合并
    # [   0.      0.   1983.72  525.69    0.   1983.72  525.69] 示例
    # print('node_position2[1]:',node_position[1])

    node_position = np.insert(node_position, 6, values=np.zeros(node_num), axis=1)
    # [   0.      0.   1983.72  525.69    0.   1983.72    0.    525.69] 示例
    # 共有6个元素，包括时间，节点编号，当前x坐标，当前y坐标，目的位置x坐标，目的位置y坐标,节点移动速度

    plt.ion()
    nodelist = []
    com_nodelist = []
    controller = Init.init_controller(node_num)
    # print(controller.node_info_dict)

    rsus = Server.gen_rsu()  # 生成路边服务器rsu
    # print(len(rsus))
    x_max = round(x_max)
    y_max = round(y_max)
    print('x , y , s:', x_max, y_max, x_max * y_max)
    x_position = random.sample(range(0, x_max), 500)
    y_position = random.sample(range(0, y_max), 500)
    for i in range(len(rsus)):  # 为服务器随机选择地点
        rsus[i].position_x = x_position[i]
        rsus[i].position_y = y_position[i]
        print('id:{0},x:{1},y:{2},file:{3}'.format(rsus[i].id,rsus[i].position_x,rsus[i].position_y,rsus[i].file))

    controller.rsus = rsus  # 绑定到控制器中
    controller.mbs = Server.MBS()
    controller.mbs.get_file_list()

    sim_time = animation
    for i in range(0, sim_time + 1):
        update_node_position(movement_matrix, node_position, i, 0.01, animation, nodelist, com_nodelist, controller)
        print(nodelist)
    print("exiting......")
    return nodelist




# 图形化界面
import ui.QT_demo as UI
import ui.chart as chart
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtChart import *
import sys,os

movies = []
with open('D:\Project\python\DEMO\data\data.txt', 'r', encoding='utf-8') as f:
    movies = f.readlines()

def start_coding():
    animation = int(mw.TimeSelect.currentText())
    nodes = control_movement(animation)
    for node in nodes:
        mw.Vehicle_view.addItem("车辆结点"+str(node.node_id))
        # print(node.latency)
    mw.Vehicle_view.clicked.connect(lambda:display_content(nodes))
    # print(node)

def display_content(nodes):
    mw.content_view.clear()
    c_v = int(mw.Vehicle_view.currentItem().text()[4:])
    # mw.content_view.addItems(nodes[c_v-1])
    mw.content_view.addItems(nodes[c_v-1].request_list[0])
    mw.content_view.clicked.connect(content_all)
    # print(nodes[c_v-1].latency)
    mw.latency.clicked.connect(lambda :chart_view(nodes[c_v-1].latency))

def chart_view(point_list):
    # mw.chartview.clear()
    print(point_list)
    p_list = []
    # mw.chartview.chart().clear()
    i = 1
    for point in point_list:
        point = QPointF(i , point)
        i += 1
        p_list.append(point)
    # mw.series = QLineSeries()
    # mw.x_Aix = QValueAxis()
    # mw.y_Aix = QValueAxis()
    mw.series.replace(p_list)
    # mw.series.setName("延迟分析")
    mw.x_Aix.setRange(0.00 , len(point_list))
    mw.y_Aix.setRange(min(point_list) , max(point_list))
    mw.x_Aix.setLabelFormat("%0.2f")
    mw.y_Aix.setLabelFormat("%0.5f")

    mw.x_Aix.setTickCount(3)
    mw.x_Aix.setMinorTickCount(0)
    mw.y_Aix.setTickCount(3)
    mw.y_Aix.setMinorTickCount(0)
    # print("True")
    # mw.chartview.chart().clear()
    mw.chartview.chart().addSeries(mw.series)
    mw.chartview.chart().setAxisX(mw.x_Aix)
    mw.chartview.chart().setAxisY(mw.y_Aix)
    mw.chartview.show()
    # mw.Vehicle_view.clicked.connect(lambda:display_content(nodes))

def content_all():
    Text = mw.content_view.currentItem().text()
    for item in movies:
        if Text[3:] in item:
            print(item)
            information = item.split()
            QMessageBox.information(mw.content_view,"详细信息",
                                    "电影名称:" + information[1][3:] + "\n上映日期：" + information[2] + "\n国家/评分：" + information[3]+information[4])
            break

def view_film():
    start_directory = r'D:\Project\python\DEMO'
    os.system("explorer.exe %s" % start_directory)

def showtime():
    time = QDateTime.currentDateTime()  # 获取当前时间
    timedisplay = time.toString("yyyy-MM-dd hh:mm:ss dddd")  # 格式化一下时间
    mw.label1.setText(timedisplay)

def clear_chart(mw):
    mw.series.clear()

def get_chart():
    window = QDialog()
    chart_window = chart.Ui_Dialog()
    chart_window.setupUi(window)
    window.setWindowTitle("饼状图")
    window.show()
    if window.exec_() == QDialog.Accepted:
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainwindow = QDialog()
    mw = UI.Ui_Dialog()
    mw.setupUi(mainwindow)

    mw.TimeSelect.addItems([str(i + 1) for i in range(309)])

    mw.simulation.clicked.connect(start_coding)
    mw.movies.clicked.connect(view_film)
    mw.timer.timeout.connect(showtime)
    mw.chart.clicked.connect(get_chart)
    # mw.content_view.itemClicked.connect(clicked)

    mainwindow.show()
    sys.exit(app.exec_())
    # control_movement(1)
