import Node as Nd
import SDVN_Controller as Sc
import random
import Global_Par as Gp
import networkx as nx


# 初始化,创建节点对象,并将各个节点的初始位置和节点编号赋值
def init_node(node_id_position, controller):
    node_list = []
    for i in range(node_id_position.shape[0]):
        node_list.append(Nd.Node(int(node_id_position[i][0, 0]), controller))
        # print('结点编号：%d'%node_id_position[i][0,0])
    return node_list


def init_controller(node_num):
    G = nx.DiGraph()
    return Sc.SDVNController(G, node_num)


# 获取通信的节点,node_num为节点数量,com_node_rate为通信节点的比例,round四舍五入  ?
def get_communication_node(node_num):
    n = round((node_num * Gp.com_node_rate)/2) * 2
    com_nodelist = []
    for i in range(node_num):
        if len(com_nodelist) < n:
            node_id = round(random.random() * node_num)
            if node_id not in com_nodelist and (node_id < 1 or node_id > 3):
                com_nodelist.append(node_id)
        else:
            break
    return [com_nodelist[i:i+2] for i in range(0, n, 2)]


# 获取通信的节点,node_num为节点数量,com_node_rate为通信节点的比例
def geo_get_communication_node(node_num, num):
    n = round((node_num * Gp.com_node_rate)/2) * 2
    com_nodelist = []
    for i in range(node_num):
        if len(com_nodelist) < n:
            node_id = round(random.random() * node_num)
            if node_id not in com_nodelist and (node_id < 1 or node_id > 3):
                com_nodelist.append(node_id)
        else:
            break
    des = [[] for i in range(node_num)]
    for i in range(node_num):
        while True:
            if len(des[i]) != num:
                node_id = round(random.random() * node_num)
                if node_id == i:
                    continue
                if node_id not in des[i] and (node_id < 1 or node_id > 3):
                    des[i].append(node_id)
                    continue
            else:
                break
    return com_nodelist, des

