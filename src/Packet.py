# 信息更新包 属性：id，地理位置，速度，加速度，当前剩余缓存
class Hello:
    def __init__(self, node_id, position, velocity, direction, acceleration, current_cache):
        self.node_id = node_id
        self.position = position
        self.velocity = velocity
        self.direction = direction
        self.acceleration = acceleration
        self.current_cache = current_cache


# 路由请求 属性：源节点，目的节点，发出者节点，发出者序号
class FlowRequest:
    def __init__(self, source_id, des_id, node_id, seq):
        self.source_id = source_id
        self.des_id = des_id
        self.seq = seq
        self.node_id = node_id


# 路由回复 属性：源节点，目的节点，路径节点序列，路由发出者节点，路由发出者序号
class FlowReply:
    def __init__(self, source_id, des_id, route, node_id, seq):
        self.source_id = source_id
        self.des_id = des_id
        self.route = route
        self.seq = seq
        self.node_id = node_id

# 路由回复 属性：源节点，目的节点，路径节点序列，路由发出者节点，路由发出者序号
class geo_FlowReply:
    def __init__(self, source_id, des_list, nexthoplist, node_id, seq):
        self.source_id = source_id
        self.des_list = des_list
        self.nexthoplist = nexthoplist
        self.seq = seq
        self.node_id = node_id

# 路由错误请求 属性： 源节点，目的节点，错误节点，错误次数，路由发出者序号，错误发出者序号
class FlowError:
    def __init__(self, source_id, des_id, error_id, time, source_seq, error_seq):
        self.source_id = source_id
        self.des_id = des_id
        self.error_id = error_id
        self.time = time
        self.source_seq = source_seq
        self.error_seq = error_seq


# 数据分组 属性：源节点，目的节点，分组大小，状态，路由发出者节点，路由发出者序号
class DataPkt:
    def __init__(self, source_id, des_id, pkt_size, state, node_id, seq, s_time):
        self.source_id = source_id
        self.des_id = des_id
        self.pkt_size = pkt_size
        self.state = state
        self.seq = seq
        self.node_id = node_id
        self.s_time = s_time
        self.e_time = 0
        self.delay = 0

# 数据分组 属性：源节点，目的节点，分组大小，状态，路由发出者节点，路由发出者序号
class geo_DataPkt:
    def __init__(self, source_id, des_list, pkt_size, state, node_id, seq, s_time):
        self.source_id = source_id
        self.des_list = des_list
        self.pkt_size = pkt_size
        self.state = state
        self.seq = seq
        self.node_id = node_id
        self.s_time = s_time
        self.e_time = 0
        self.delay = 0


class geo_FlowRequest:
    def __init__(self, source_id, des_list, node_id, seq):
        self.source_id = source_id
        self.des_list = des_list
        self.seq = seq
        self.node_id = node_id

# 路由表 属性：源节点，目的节点，下一跳节点，状态，路由发出者节点，路由发出者序号
class RoutingTable:
    def __init__(self, source_id, des_id, next_hop_id, state, node_id, seq):
        self.source_id = source_id
        self.des_id = des_id
        self.next_hop_id = next_hop_id
        self.state = state
        self.seq = seq
        self.node_id = node_id

