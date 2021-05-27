import numpy as np
import math

def simulation(node_id_position,nodelist,com_nodelist,i,controller):

    for rsu in controller.rsus:
        rsu.veihcle.clear()
    for node in nodelist:
        id = node.node_id
        # print('current node:',id)
        if len(node.cache) == 20:
            node.request_list[0] = node.cache[:]
            node.cache.clear()
            node.history.append(node.request_list[0])
            print(id,node.request_list[0])
            print(node.train_cache)
        flag = 0
        x = node_id_position[id,1]
        y = node_id_position[id,2]
        for rsu in controller.rsus:
            if math.sqrt((rsu.position_x - x)**2 + (rsu.position_y - y)**2) < 300:
                if len(rsu.veihcle)<rsu.capacity:
                    rsu.veihcle.append(node)
                    node.rsu_id = rsu.id
                    break

        rsu = controller.rsus[node.rsu_id]
        # print('train_cache',node.train_cache)
        for veh in rsu.veihcle:
            if veh != node:
                for request in node.train_cache:
                    for request_list in veh.request_list[0]:
                        # print(request_list)
                        if request in request_list:
                            if len(node.cache) < 20:
                                node.cache.append(request_list)
                                node.cache = list(set(node.cache))
                                # node.history.append(node.cache)
                                l = d2d_latency(x,y,node_id_position[veh.node_id,1],node_id_position[veh.node_id,2])
                                if node.max_latency < l:
                                    node.max_latency = l
                                # print(node.node_id,node.rsu_id,l)
                                node.latency.append(l)
                                # print(node.latency)
                                flag = 1
                                break
                    if flag == 1:
                        break
        if flag == 0:
            for request in node.train_cache:
                for file in rsu.file:
                    if request in file:
                        if len(node.cache) < 20:
                            node.cache.append(file)
                            node.cache = list(set(node.cache))
                            l = rsu_latency(x, y, rsu.position_x, rsu.position_y)
                            # print(node.node_id,node.rsu_id,l)
                            node.latency.append(l)
                            if node.max_latency < l:
                                node.max_latency = l
                            # node.history.append(node.cache)
                            # print(node.latency)
                            flag = 1
                            break
        if flag == 0:
            # print('find content in MBS!')
            # for request in node.train_cache:
            #     index = controller.mbs.movie_type.value(request)
            pass


def d2d_latency(source_x , source_y , dest_x , dest_y):
    pd = 0.25
    k = 0.01
    e = 10**(-17.4)*10
    gd2d = k*math.sqrt((source_x - dest_x)**2+(source_y - dest_y)**2)*0.0001
    snr = pd * gd2d / e
    wd2d = 10*math.log(1+snr,2)
    if wd2d == 0:
        latency = 0
    else:latency = 10/wd2d
    return latency

def rsu_latency(source_x , source_y , dest_x , dest_y):
    pd = 0.25
    k = 0.01
    e = 10**(-17.4)*10
    gd2d = k*math.sqrt((source_x - dest_x)**2+(source_y - dest_y)**2)*0.0001
    snr = pd * gd2d / e
    w = 10*math.log(1+snr,2)
    latency = 30/w
    return latency