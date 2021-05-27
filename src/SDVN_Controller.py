import Packet as Pkt
import Global_Par as Gp
import dij_test1 as dij
import networkx as nx
import mcds


class SDVNController:
    def __init__(self, junction_matrix, node_num):
        self.hello_list = []  # hello请求列表
        self.flow_request_list = []  # 路由请求列表
        self.geo_flow_request_list = []
        self.flow_error_list = []  # 错误请求列表
        self.junction_matrix = junction_matrix  # 邻接矩阵,这是一个图
        self.node_info_dict = {i: [[], [], [], ] for i in range(node_num)}  # 所有节点信息
        self.exp_nodes = {}
        self.rsus = []
        self.mbs = None





    # 根据hello列表中的条目更新控制器中的节点信息
    # 预测位置？
    def predict_position(self):
        for value in self.hello_list:
            self.node_info_dict[value.node_id] = [value.position,  value.velocity, value.direction, value.acceleration, value.current_cache]
        self.hello_list.clear()
        return

    def junction_matrix_construction(self, node_num):
        self.junction_matrix.clear()
        for i in range(0, node_num):
            for j in range(0, i):
                a = pow(self.node_info_dict[i][0][0] - self.node_info_dict[j][0][0], 2) + pow(self.node_info_dict[i][0][1] - self.node_info_dict[j][0][1], 2)
                if a < pow(Gp.com_dis, 2):
                    self.junction_matrix.add_edge(i, j, weight=a)
                    self.junction_matrix.add_edge(j, i, weight=a)


    # 根据节点信息计算路由
    def calculate_path(self, x_id, des_id, node_list,node_num):
        # dijkstra
        route = dij.Dijkstra(self.junction_matrix, x_id, des_id)
        if route:
            print(route)
            return route
        print('%d to %d calculation error' % (x_id, des_id))
        return [x_id, des_id]


    @staticmethod
    def geo_calculate_path(x_id, des_list, node_list):
        sub = des_list
        sub.append(x_id)
        G = nx.Graph()
        for a in sub:
            for b in sub:
                if a == 381:
                    a = a-1
                if b == 381:
                    b = b-1
                if a != b:
                    d = pow(node_list[a].position[0] - node_list[b].position[0], 2) + pow(
                        node_list[a].position[1] - node_list[b].position[1], 2)
                    G.add_edge(a, b, weight = d)
        un = des_list
        visited = [x_id]
        next_hop = [[] for i in range(len(node_list))]
        mcds.dfs(G, x_id, visited, un, next_hop)
        return visited,next_hop


    # 向路由上的每个节点发送路由回复
    @staticmethod
    def send_reply(x_id, des_id, route, node_list, node_id, seq):
        flow_reply = Pkt.FlowReply(x_id, des_id, route, node_id, seq)
        for node_num in route:
            node_list[node_num].receive_flow(flow_reply)
    # 时延处理
        return

    @staticmethod
    def geo_send_reply(x_id, des_list, associated_node, next_hop_list, node_list, node_id, seq):
        for node in associated_node:
            flow_reply = Pkt.geo_FlowReply(x_id, des_list, next_hop_list[node], node_id, seq)
            node_list[node].geo_receive_flow(flow_reply)
        # 时延处理
        return

    # 处理请求表中的每个请求，计算路由，发送回复
    def resolve_request(self, node_list):
        for request in self.flow_request_list:
            route = self.calculate_path(request.source_id, request.des_id, node_list,len(node_list))
            self.send_reply(request.source_id, request.des_id, route, node_list, request.node_id, request.seq)
        self.flow_request_list.clear()
        return

    def geo_resolve_request(self, node_list):
        for request in self.geo_flow_request_list:
            associated_node, next_hop_list = self.geo_calculate_path(request.source_id, request.des_list, node_list)
            self.geo_send_reply(request.source_id, request.des_list, associated_node, next_hop_list, node_list, request.node_id, request.seq)
        self.geo_flow_request_list.clear()
        return

    # 删除路由信息（超过三次需要删除所有相关路由信息与分组）
    def delete_routing_pkt(self, node_list, source_id, id, seq, des_id):
        # 到达目的节点后，删除相关信息并返回
        if id == des_id:
            for table in node_list[id].routing_table[::-1]:
                if table.seq == seq and table.node_id == source_id:
                    # print('node %d routing delete' % id)
                    node_list[id].routing_table.remove(table)
            for pkt in node_list[id].data_pkt_list[::-1]:
                if pkt.seq == seq and pkt.node_id == source_id:
                    # print('node %d pkt delete' % id)
                    node_list[id].data_pkt_list.remove(pkt)
            return
        # 未到达目的节点，根据路由表递归地删除。
        for table in node_list[id].routing_table[::-1]:
            if table.seq == seq and table.node_id == source_id:
                self.delete_routing_pkt(node_list, source_id, table.next_hop_id, seq, des_id)
                # print('node %d routing delete' % id)
                node_list[id].routing_table.remove(table)
        for pkt in node_list[id].data_pkt_list[::-1]:
            if pkt.seq == seq and pkt.node_id == source_id:
                # print('node %d pkt delete' % id)
                node_list[id].data_pkt_list.remove(pkt)

    # 解析错误请求信息
    def resolve_error(self, node_list):
        # 对错误请求列表里的所有节点处理
        for error in self.flow_error_list[::-1]:
            # 同一跳错误次数大于N次，此条路由失败
            if error.time > Gp.re_time:
                # print('%3d to %3d 路由失败 %3d %3d' % (error.error_id, error.des_id, error.source_id, error.source_seq))
                # 删除相关路由
                self.delete_routing_pkt(node_list, error.source_id, error.error_id, error.source_seq, error.des_id)
                Gp.fail_time = Gp.fail_time + 1
                # print('source %d seq %d des %d err %d' % (error.source_id, error.source_seq, error.des_id, error.error_id))
                # print('delete\n')
                self.flow_error_list.remove(error)
        # 不然计算路由， 向下下发
        for error1 in self.flow_error_list:
            route = self.calculate_path(error1.error_id, error1.des_id, node_list,len(node_list))
            self.send_reply(error1.error_id, error1.des_id, route, node_list, error1.source_id, error1.source_seq)
        return
