import Packet as Pkt
import Global_Par as Gp
import jhmmtg as jh
import time
import proba as pr
import math
import MAB


class Node:
    def __init__(self, node_id, controller):
        self.node_id = node_id  # 节点id
        self.position = [0, 0, 0]  # 位置 三维
        self.direction = [0, 0, 0]  # 方向
        self.velocity = [0, 0, 0]  # 速度
        self.routing_table = []  # 路由表
        self.geo_routing_table = []
        self.data_pkt_list = []  # 数据分组存储
        self.cache = []  # 当前缓存
        self.controller = controller  # 自身所属控制器
        self.pkt_seq = 0  # 当前节点包序号
        self.junction = []
        self.grid = -1
        self.dx = True
        self.dy = True
        self.dz = True
        self.IMN = -1  # 节点的影响力最大化节点
        self.request_list = MAB.get_file()
        self.train_cache = []
        self.cache_capacity = 20
        self.rsu_id = -1 #节点当前所属rsu
        #延迟部分
        self.latency = []
        self.max_latency = 0
        self.min_latency = 10000
        self.history = []
        self.mean_latency = []
        # self.chart = []

    #训练数据，得到应该请求的类型
    def request_cache(self):
        mab = MAB.MAB()
        current_cache = []
        self.train_cache = []
        for node in self.request_list[0]:
            current_cache.append(node[0:2])#取出缓存中电影的类型
        action,action_num,kind = mab.e_greedy(current_cache)
        # print('kind,action,action_num:\n',kind,action,action_num)
        # print('node_id:',self.node_id)
        for i in range(kind):
            if action_num[i] >= 0.1:#如果比例小于0.1代表用户申请该类型的数据少
                self.train_cache.append(action[i])#将该类型加入到训练后的缓存里
        # print('training:\n',self.train_cache)


    def get_mean_latency(self):
        lenth = len(self.latency)
        sum = 0
        for point in self.latency:
            sum += point
        return sum/lenth


    def get_com_node_list(self,node_position):
        for node in node_position:
            if self.node_id in node:
                print(node)

    def v2v_content_cache(self , source_id , latency , content , time):
        hello = ['所属RSU'+ self.rsu_id + '内容来源' + source_id + '延迟' + latency + '内容' + content + '时间' + time]
        self.history.append(hello)

    # 根据数据更新自身位置
    def update_node_position(self, node_id_position):
        self.velocity[0] = node_id_position[self.node_id][0, 0] - self.position[0]
        self.velocity[1] = node_id_position[self.node_id][0, 1] - self.position[1]
        self.velocity[2] = node_id_position[self.node_id][0, 2] - self.position[2]
        self.position = [node_id_position[self.node_id][0, 0], node_id_position[self.node_id][0, 1], node_id_position[self.node_id][0, 2]]
        if self.velocity[0] < 0:
            self.dx = False
        if self.velocity[1] < 0:
            self.dy = False
        if self.velocity[2] < 0:
            self.dz = False
        self.direction = [self.dx, self.dy, self.dz]
        # self.junction = jh.junction_judge(self.position[0], self.position[1], self.node_id)
        return

    def drone_update_position(self, pass_time):
        self.position[0] = self.position[0] + self.velocity[0] * pass_time
        self.position[1] = self.position[1] + self.velocity[1] * pass_time
        self.position[2] = self.position[2] + self.velocity[2] * pass_time

    # 产生数据包
    def generate_hello(self, controller):
        # 时延处理
        controller.hello_list.append(Pkt.Hello(self.node_id,  self.position,  self.velocity, self.direction,
                                               self.acceleration,  self.cache))
        return

    # 产生数据包，且向控制器发送请求，自身序号加1
    def generate_request(self,  des_id, controller, size):
        # 时延处理
        print('node %d generate packet to node %d' % (self.node_id, des_id))
        self.data_pkt_list.append(Pkt.DataPkt(self.node_id, des_id, size, 0, self.node_id, self.pkt_seq, time.time()))
        controller.flow_request_list.append(Pkt.FlowRequest(self.node_id,  des_id, self.node_id, self.pkt_seq))
        self.pkt_seq = self.pkt_seq + 1
        return

    # 产生数据包，且向控制器发送请求，自身序号加1
    def generate_geo_request(self,  des_list, controller, size):
        # 时延处理
        self.data_pkt_list.append(Pkt.geo_DataPkt(self.node_id, des_list, size, 0, self.node_id, self.pkt_seq, time.time()))
        controller.geo_flow_request_list.append(Pkt.geo_FlowRequest(self.node_id, des_list, self.node_id, self.pkt_seq))
        self.pkt_seq = self.pkt_seq + 1
        return

    # 发送错误请求
    def generate_error(self,  source_id,  des_id, controller, seq, node_list):
        # 根据发送者节点和序号确定此错误路由是否存在，存在即错误次数加1
        for error in controller.flow_error_list:
            if error.source_id == source_id and error.source_seq == seq:
                error.time = error.time + 1
                return
        # 时延处理
        # 控制器增加此错误路由
        controller.flow_error_list.append(Pkt.FlowError(source_id,  des_id,  self.node_id, 1, seq, seq))
        self.pkt_seq = self.pkt_seq + 1
        return

    # 处理路由回复（均用发送者节点和序号确定路由信息所属）
    def receive_flow(self, flow_reply):
        # 如果已到达目的节点，路由表增加一个以自己为下一跳节点的条目
        if flow_reply.des_id == self.node_id:
            self.routing_table.append(Pkt.RoutingTable(flow_reply.source_id, flow_reply.des_id, flow_reply.des_id, 0, flow_reply.node_id, flow_reply.seq))
            return

        # 如果此条目已存在，更新信息
        for t in self.routing_table:
            if t.seq == flow_reply.seq and t.node_id == flow_reply.node_id:
                for key, node_id in enumerate(flow_reply.route):
                    if node_id == self.node_id:
                        t.next_hop_id = (flow_reply.route[key + 1])
                        return

        # 增加新的路由条目
        for key, node_id in enumerate(flow_reply.route):
            if node_id == self.node_id:
                self.routing_table.append(Pkt.RoutingTable(flow_reply.source_id, flow_reply.des_id, flow_reply.route[key+1], 0, flow_reply.node_id, flow_reply.seq))
                return

    # 处理路由回复（均用发送者节点和序号确定路由信息所属）
    def geo_receive_flow(self, geo_flow_reply):
        # 如果已到达目的节点，路由表增加一个以自己为下一跳节点的条目
        if len(geo_flow_reply.nexthoplist) == 0:
            self.routing_table.append(Pkt.RoutingTable(geo_flow_reply.source_id, self.node_id, self.node_id, 0, geo_flow_reply.node_id, geo_flow_reply.seq))
            return

        # 如果此条目已存在，更新信息
        for t in self.routing_table[::-1]:
            if t.seq == geo_flow_reply.seq and t.node_id == geo_flow_reply.node_id:
                self.routing_table.remove(t)

        for i in geo_flow_reply.nexthoplist:
            self.routing_table.append(Pkt.RoutingTable(geo_flow_reply.source_id, 9999, i, 0, geo_flow_reply.node_id, geo_flow_reply.seq))

    # 根据自己的路由表转发自身携带分组
    def forward_pkt_to_nbr(self, node_list, controller):
        for pkt in self.data_pkt_list[::-1]:
            for table in self.routing_table[::-1]:
                # 如果路由表条目与分组相符
                if pkt.seq == table.seq and pkt.node_id == table.node_id:
                    # 转发成功与否判断
                    d = pow(node_list[table.next_hop_id].position[0] - self.position[0], 2) + pow(
                        node_list[table.next_hop_id].position[1] - self.position[1], 2)
                    # 转发成功与否判断
                    if d < pow(Gp.com_dis, 2):
                        # 时延计算
                        if pr.ratio(math.sqrt(d)) == 1:
                        # 下一跳节点收分组
                            node_list[table.next_hop_id].receive_pkt(pkt, node_list, controller)
                            # 改变路由条目与分组状态以删除
                            # print('%d to %d success hop\n%d routing delete' % (self.node_id, table.next_hop_id, self.node_id))
                            self.data_pkt_list.remove(pkt)
                            if self.routing_table.count(table)!=0:
                                self.routing_table.remove(table)
                            break
                        else:
                            # 时延计算
                            # 路由发生错误，回调路由条目与分组状态，发送错误请求
                            print('node %3d to node %3d 距离超过' % (self.node_id, node_list[table.next_hop_id].node_id))
                            if self.routing_table.count(table) != 0:
                                self.routing_table.remove(table)
                            self.generate_error(pkt.source_id, pkt.des_id, self.controller, pkt.seq, node_list)
                            break
                else:
                    # 时延计算
                    # 路由发生错误，回调路由条目与分组状态，发送错误请求
                    print('node %3d to node %3d 距离超过' % (self.node_id, node_list[table.next_hop_id].node_id))
                    if self.routing_table.count(table) != 0:
                        self.routing_table.remove(table)
                    self.generate_error(pkt.source_id, pkt.des_id, self.controller, pkt.seq, node_list)
                    break
        return

    # 根据自己的路由表转发自身携带分组
    def geo_forward_pkt_to_nbr(self, node_list):
        for pkt in self.data_pkt_list[::-1]:
            flag = 0
            for table in self.routing_table[::-1]:
                # 如果路由表条目与分组相符
                if pkt.seq == table.seq and pkt.node_id == table.node_id:
                    d = pow(node_list[table.next_hop_id].position[0] - self.position[0], 2) + pow(node_list[table.next_hop_id].position[1] - self.position[1], 2)
                    # 转发成功与否判断
                    if d < pow(Gp.com_dis, 2):
                        # 时延计算
                        # 下一跳节点收分组
                        pkt.state = 1
                        node_list[table.next_hop_id].geo_receive_pkt(pkt, node_list)
                        # 改变路由条目与分组状态以删除
                        # print('%d to %d success hop\n%d routing delete' % (self.node_id, table.next_hop_id, self.node_id))
                        self.routing_table.remove(table)
                    else:
                        # 时延计算
                        # 路由发生错误，回调路由条目与分组状态，发送错误请求
                        print('node %3d to node %3d 距离超过' % (self.node_id, node_list[table.next_hop_id].node_id))
                        self.generate_error(pkt.source_id, table.next_hop_id, self.controller, pkt.seq, node_list)
                        break
        for pkt_1 in self.data_pkt_list[::-1]:
            if pkt_1.state == 1:
                self.data_pkt_list.remove(pkt_1)
        return

    # 接受转发来的分组
    def receive_pkt(self, data_pkt, node_list, controller):
        # 到达终点 转发成功
        data_pkt.delay += 0.03
        if data_pkt.des_id == self.node_id:
            data_pkt.e_time = time.time()
            for error in controller.flow_error_list[::-1]:
                if data_pkt.node_id == error.source_id and data_pkt.seq == error.source_seq:
                    controller.flow_error_list.remove(error)
            print('%3d to %3d successful transmission！' % (data_pkt.source_id, data_pkt.des_id))
            print(data_pkt.e_time - data_pkt.s_time + data_pkt.delay)
            Gp.sum = Gp.sum + (data_pkt.e_time - data_pkt.s_time + data_pkt.delay)
            Gp.record.append(data_pkt.e_time - data_pkt.s_time + data_pkt.delay)
            # 时延总计算
            # 丢包率计算
            return
        # 自己添加改包 并继续转发

        self.data_pkt_list.append(data_pkt)
        self.forward_pkt_to_nbr(node_list, controller)
        return

    # 接受转发来的分组
    def geo_receive_pkt(self, data_pkt, node_list):
        # 到达终点 转发成功
        for table in self.routing_table[::-1]:
            if data_pkt.node_id == table.node_id and data_pkt.seq == table.seq:
                if table.next_hop_id == table.des_id:
                    data_pkt.e_time = time.time()
                    print('%3d to %3d successful transmission！' % (data_pkt.source_id, self.node_id))
                    print(data_pkt.e_time - data_pkt.s_time + data_pkt.delay)
                    Gp.sum = Gp.sum + (data_pkt.e_time - data_pkt.s_time + data_pkt.delay)
                    Gp.record.append(data_pkt.e_time - data_pkt.s_time + data_pkt.delay)
                    # 时延总计算
                    # 丢包率计算
                    return
            # 自己添加改包 并继续转发
        print('%d node receive!' % self.node_id)
        self.data_pkt_list.append(data_pkt)
        self.geo_forward_pkt_to_nbr(node_list)
        return

