import junction_init as ji
# import q_learning as ql
import networkx as nx
import dij_test1 as dij
import Global_Par as Gp

alpha = 0.5
beta = 1 - alpha


def insort_right(a, x, lo=0, hi=None):
    """Insert item x in list a, and keep it sorted assuming a is sorted.

    If x is already in a, insert it to the right of the rightmost x.

    Optional args lo (default 0) and hi (default len(a)) bound the
    slice of a to be searched.
    """

    if lo < 0:
        raise ValueError('lo must be non-negative')
    if hi is None:
        hi = len(a)
    while lo < hi:
        mid = (lo+hi)//2
        if x.t < a[mid].t:
            hi = mid
        else:
            lo = mid+1
    a.insert(lo, x)


class edge:
    def __init__(self, u, v, t, d):
        self.u = u  # hello请求列表
        self.v = v  # 路由请求列表
        self.t = t  # 错误请求列表
        self.d = d  # 邻接矩阵


def junction_judge(x, y, node_id):
    if y < 178.45:
        if x < 170.9:
            ji.junction_vehicle[0].append(node_id)
            if abs(x - 0) > abs(y - 0):
                if x > 0:
                    ji.veh_segement_martix[0][1].append(node_id)
                    return 0, 1
                if x < 0:
                    ji.veh_segement_martix[0][3].append(node_id)
                    return 0, 3
            if abs(x - 0) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[0][0].append(node_id)
                    return 0, 0
                if y < 0:
                    ji.veh_segement_martix[0][2].append(node_id)
                    return 0, 2
        if x < 463.4:
            ji.junction_vehicle[1].append(node_id)
            if abs(x - 341.8) > abs(y - 0):
                if x > 341.8:
                    ji.veh_segement_martix[1][1].append(node_id)
                    return 1, 1
                if x < 341.8:
                    ji.veh_segement_martix[1][3].append(node_id)
                    return 1, 3
            if abs(x - 341.8) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[1][0].append(node_id)
                    return 1, 0
                if y < 0:
                    ji.veh_segement_martix[1][2].append(node_id)
                    return 1, 2
        if x < 694.05:
            ji.junction_vehicle[2].append(node_id)
            if abs(x - 585) > abs(y - 0):
                if x > 585:
                    ji.veh_segement_martix[2][1].append(node_id)
                    return 2, 1
                if x < 585:
                    ji.veh_segement_martix[2][3].append(node_id)
                    return 2, 3
            if abs(x - 585) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[2][0].append(node_id)
                    return 2, 0
                if y < 0:
                    ji.veh_segement_martix[2][2].append(node_id)
                    return 2, 2
        if x < 991.1:
            ji.junction_vehicle[3].append(node_id)
            if abs(x - 803.1) > abs(y - 0):
                if x > 803.1:
                    ji.veh_segement_martix[3][1].append(node_id)
                    return 3, 1
                if x < 803.1:
                    ji.veh_segement_martix[3][3].append(node_id)
                    return 3, 3
            if abs(x - 803.1) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[3][0].append(node_id)
                    return 3, 0
                if y < 0:
                    ji.veh_segement_martix[3][2].append(node_id)
                    return 3, 2
        if x < 1286.9:
            ji.junction_vehicle[4].append(node_id)
            if abs(x - 1179.1) > abs(y - 0):
                if x > 1179.1:
                    ji.veh_segement_martix[4][1].append(node_id)
                    return 4, 1
                if x < 1179.1:
                    ji.veh_segement_martix[4][3].append(node_id)
                    return 4, 3
            if abs(x - 1179.1) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[4][0].append(node_id)
                    return 4, 0
                if y < 0:
                    ji.veh_segement_martix[4][2].append(node_id)
                    return 4, 2
        if x < 1514.8:
            ji.junction_vehicle[5].append(node_id)
            if abs(x - 1394.7) > abs(y - 0):
                if x > 1394.7:
                    ji.veh_segement_martix[5][1].append(node_id)
                    return 5, 1
                if x < 1394.7:
                    ji.veh_segement_martix[5][3].append(node_id)
                    return 5, 3
            if abs(x - 1394.7) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[5][0].append(node_id)
                    return 5, 0
                if y < 0:
                    ji.veh_segement_martix[5][2].append(node_id)
                    return 5, 2
        if x < 1798:
            ji.junction_vehicle[6].append(node_id)
            if abs(x - 1634.9) > abs(y - 0):
                if x > 1634.9:
                    ji.veh_segement_martix[6][1].append(node_id)
                    return 6, 1
                if x < 1634.9:
                    ji.veh_segement_martix[6][3].append(node_id)
                    return 6, 3
            if abs(x - 1634.9) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[6][0].append(node_id)
                    return 6, 0
                if y < 0:
                    ji.veh_segement_martix[6][2].append(node_id)
                    return 6, 2
        if x < 2086.35:
            ji.junction_vehicle[7].append(node_id)
            if abs(x - 1961.1) > abs(y - 0):
                if x > 1961.1:
                    ji.veh_segement_martix[7][1].append(node_id)
                    return 7, 1
                if x < 1961.1:
                    ji.veh_segement_martix[7][3].append(node_id)
                    return 7, 3
            if abs(x - 1961.1) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[7][0].append(node_id)
                    return 7, 0
                if y < 0:
                    ji.veh_segement_martix[7][2].append(node_id)
                    return 7, 2
        if x < 2385.4:
            ji.junction_vehicle[8].append(node_id)
            if abs(x - 2211.6) > abs(y - 0):
                if x > 2211.6:
                    ji.veh_segement_martix[8][1].append(node_id)
                    return 8, 1
                if x < 2211.6:
                    ji.veh_segement_martix[8][3].append(node_id)
                    return 8, 3
            if abs(x - 2211.6) <= abs(y - 0):
                if y > 0:
                    ji.veh_segement_martix[8][0].append(node_id)
                    return 8, 0
                if y < 0:
                    ji.veh_segement_martix[8][2].append(node_id)
                    return 8, 2
        ji.junction_vehicle[9].append(node_id)
        if abs(x - 2559.2) > abs(y - 0):
            if x > 2559.2:
                ji.veh_segement_martix[9][1].append(node_id)
                return 9, 1
            if x < 2559.2:
                ji.veh_segement_martix[9][3].append(node_id)
                return 9, 3
        if abs(x - 2559.2) <= abs(y - 0):
            if y > 0:
                ji.veh_segement_martix[9][0].append(node_id)
                return 9, 0
            if y < 0:
                ji.veh_segement_martix[9][2].append(node_id)
                return 9, 2

    if y < 432.9:
        if x < 170.9:
            ji.junction_vehicle[10].append(node_id)
            if abs(x - 0) > abs(y - 356.9):
                if x > 0:
                    ji.veh_segement_martix[10][1].append(node_id)
                    return 10, 1
                if x < 0:
                    ji.veh_segement_martix[10][3].append(node_id)
                    return 10, 3
            if abs(x - 0) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[10][0].append(node_id)
                    return 10, 0
                if y < 356.9:
                    ji.veh_segement_martix[10][2].append(node_id)
                    return 10, 2
        if x < 463.4:
            ji.junction_vehicle[11].append(node_id)
            if abs(x - 341.8) > abs(y - 356.9):
                if x > 341.8:
                    ji.veh_segement_martix[11][1].append(node_id)
                    return 11, 1
                if x < 341.8:
                    ji.veh_segement_martix[11][3].append(node_id)
                    return 11, 3
            if abs(x - 341.8) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[11][0].append(node_id)
                    return 11, 0
                if y < 356.9:
                    ji.veh_segement_martix[11][2].append(node_id)
                    return 11, 2
        if x < 694.05:
            ji.junction_vehicle[12].append(node_id)
            if abs(x - 585) > abs(y - 356.9):
                if x > 585:
                    ji.veh_segement_martix[12][1].append(node_id)
                    return 12, 1
                if x < 585:
                    ji.veh_segement_martix[12][3].append(node_id)
                    return 12, 3
            if abs(x - 585) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[12][0].append(node_id)
                    return 12, 0
                if y < 356.9:
                    ji.veh_segement_martix[12][2].append(node_id)
                    return 12, 2
        if x < 991.1:

            ji.junction_vehicle[13].append(node_id)
            if abs(x - 803.1) > abs(y - 356.9):
                if x > 803.1:
                    ji.veh_segement_martix[13][1].append(node_id)
                    return 13, 1
                if x < 803.1:
                    ji.veh_segement_martix[13][3].append(node_id)
                    return 13, 3
            if abs(x - 803.1) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[13][0].append(node_id)
                    return 13, 0
                if y < 356.9:
                    ji.veh_segement_martix[13][2].append(node_id)
                    return 13, 2
        if x < 1286.9:
            ji.junction_vehicle[14].append(node_id)
            if abs(x - 1179.1) > abs(y - 356.9):
                if x > 1179.1:
                    ji.veh_segement_martix[14][1].append(node_id)
                    return 14, 1
                if x < 1179.1:
                    ji.veh_segement_martix[14][3].append(node_id)
                    return 14, 3
            if abs(x - 1179.1) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[14][0].append(node_id)
                    return 14, 0
                if y < 356.9:
                    ji.veh_segement_martix[14][2].append(node_id)
                    return 14, 2
        if x < 1514.8:
            ji.junction_vehicle[15].append(node_id)
            if abs(x - 1394.7) > abs(y - 356.9):
                if x > 1394.7:
                    ji.veh_segement_martix[15][1].append(node_id)
                    return 15, 1
                if x < 1394.7:
                    ji.veh_segement_martix[15][3].append(node_id)
                    return 15, 3
            if abs(x - 1394.7) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[15][0].append(node_id)
                    return 15, 0
                if y < 356.9:
                    ji.veh_segement_martix[15][2].append(node_id)
                    return 15, 2
        if x < 1798:
            ji.junction_vehicle[16].append(node_id)
            if abs(x - 1634.9) > abs(y - 356.9):
                if x > 1634.9:
                    ji.veh_segement_martix[16][1].append(node_id)
                    return 16, 1
                if x < 1634.9:
                    ji.veh_segement_martix[16][3].append(node_id)
                    return 16, 3
            if abs(x - 1634.9) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[16][0].append(node_id)
                    return 16, 0
                if y < 356.9:
                    ji.veh_segement_martix[16][2].append(node_id)
                    return 16, 2
        if x < 2086.35:
            ji.junction_vehicle[17].append(node_id)
            if abs(x - 1961.1) > abs(y - 356.9):
                if x > 1961.1:
                    ji.veh_segement_martix[17][1].append(node_id)
                    return 17, 1
                if x < 1961.1:
                    ji.veh_segement_martix[17][3].append(node_id)
                    return 17, 3
            if abs(x - 1961.1) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[17][0].append(node_id)
                    return 17, 0
                if y < 356.9:
                    ji.veh_segement_martix[17][2].append(node_id)
                    return 17, 2
        if x < 2385.4:
            ji.junction_vehicle[18].append(node_id)
            if abs(x - 2211.6) > abs(y - 356.9):
                if x > 2211.6:
                    ji.veh_segement_martix[18][1].append(node_id)
                    return 18, 1
                if x < 2211.6:
                    ji.veh_segement_martix[18][3].append(node_id)
                    return 18, 3
            if abs(x - 2211.6) <= abs(y - 356.9):
                if y > 356.9:
                    ji.veh_segement_martix[18][0].append(node_id)
                    return 18, 0
                if y < 356.9:
                    ji.veh_segement_martix[18][2].append(node_id)
                    return 18, 2
        ji.junction_vehicle[19].append(node_id)
        if abs(x - 2559.2) > abs(y - 356.9):
            if x > 2559.2:
                ji.veh_segement_martix[19][1].append(node_id)
                return 19, 1
            if x < 2559.2:
                ji.veh_segement_martix[19][3].append(node_id)
                return 19, 3
        if abs(x - 2559.2) <= abs(y - 356.9):
            if y > 356.9:
                ji.veh_segement_martix[19][0].append(node_id)
                return 19, 0
            if y < 356.9:
                ji.veh_segement_martix[19][2].append(node_id)
                return 19, 2

    if y < 590.4:
        if x < 170.9:
            ji.junction_vehicle[20].append(node_id)
            if abs(x - 0) > abs(y - 508.9):
                if x > 0:
                    ji.veh_segement_martix[20][1].append(node_id)
                    return 20, 1
                if x < 0:
                    ji.veh_segement_martix[20][3].append(node_id)
                    return 20, 3
            if abs(x - 0) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[20][0].append(node_id)
                    return 20, 0
                if y < 508.9:
                    ji.veh_segement_martix[20][2].append(node_id)
                    return 20, 2
        if x < 463.4:
            ji.junction_vehicle[21].append(node_id)
            if abs(x - 341.8) > abs(y - 508.9):
                if x > 341.8:
                    ji.veh_segement_martix[21][1].append(node_id)
                    return 21, 1
                if x < 341.8:
                    ji.veh_segement_martix[21][3].append(node_id)
                    return 21, 3
            if abs(x - 341.8) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[21][0].append(node_id)
                    return 21, 0
                if y < 508.9:
                    ji.veh_segement_martix[21][2].append(node_id)
                    return 21, 2
        if x < 694.05:
            ji.junction_vehicle[22].append(node_id)
            if abs(x - 585) > abs(y - 508.9):
                if x > 585:
                    ji.veh_segement_martix[22][1].append(node_id)
                    return 22, 1
                if x < 585:
                    ji.veh_segement_martix[22][3].append(node_id)
                    return 22, 3
            if abs(x - 585) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[22][0].append(node_id)
                    return 22, 0
                if y < 508.9:
                    ji.veh_segement_martix[22][2].append(node_id)
                    return 22, 2
        if x < 991.1:
            ji.junction_vehicle[23].append(node_id)
            if abs(x - 803.1) > abs(y - 508.9):
                if x > 803.1:
                    ji.veh_segement_martix[23][1].append(node_id)
                    return 23, 1
                if x < 803.1:
                    ji.veh_segement_martix[23][3].append(node_id)
                    return 23, 3
            if abs(x - 803.1) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[23][0].append(node_id)
                    return 23, 0
                if y < 508.9:
                    ji.veh_segement_martix[23][2].append(node_id)
                    return 23, 2
        if x < 1286.9:
            ji.junction_vehicle[24].append(node_id)
            if abs(x - 1179.1) > abs(y - 508.9):
                if x > 1179.1:
                    ji.veh_segement_martix[24][1].append(node_id)
                    return 24, 1
                if x < 1179.1:
                    ji.veh_segement_martix[24][3].append(node_id)
                    return 24, 3
            if abs(x - 1179.1) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[24][0].append(node_id)
                    return 24, 0
                if y < 508.9:
                    ji.veh_segement_martix[24][2].append(node_id)
                    return 24, 2
        if x < 1514.8:
            ji.junction_vehicle[25].append(node_id)
            if abs(x - 1394.7) > abs(y - 508.9):
                if x > 1394.7:
                    ji.veh_segement_martix[25][1].append(node_id)
                    return 25, 1
                if x < 1394.7:
                    ji.veh_segement_martix[25][3].append(node_id)
                    return 25, 3
            if abs(x - 1394.7) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[25][0].append(node_id)
                    return 25, 0
                if y < 508.9:
                    ji.veh_segement_martix[25][2].append(node_id)
                    return 25, 2
        if x < 1798:
            ji.junction_vehicle[26].append(node_id)
            if abs(x - 1634.9) > abs(y - 508.9):
                if x > 1634.9:
                    ji.veh_segement_martix[26][1].append(node_id)
                    return 26, 1
                if x < 1634.9:
                    ji.veh_segement_martix[26][3].append(node_id)
                    return 26, 3
            if abs(x - 1634.9) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[26][0].append(node_id)
                    return 26, 0
                if y < 508.9:
                    ji.veh_segement_martix[26][2].append(node_id)
                    return 26, 2
        if x < 2086.35:
            ji.junction_vehicle[27].append(node_id)
            if abs(x - 1961.1) > abs(y - 508.9):
                if x > 1961.1:
                    ji.veh_segement_martix[27][1].append(node_id)
                    return 27, 1
                if x < 1961.1:
                    ji.veh_segement_martix[27][3].append(node_id)
                    return 27, 3
            if abs(x - 1961.1) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[27][0].append(node_id)
                    return 27, 0
                if y < 508.9:
                    ji.veh_segement_martix[27][2].append(node_id)
                    return 27, 2
        if x < 2385.4:
            ji.junction_vehicle[28].append(node_id)
            if abs(x - 2211.6) > abs(y - 508.9):
                if x > 2211.6:
                    ji.veh_segement_martix[28][1].append(node_id)
                    return 28, 1
                if x < 2211.6:
                    ji.veh_segement_martix[28][3].append(node_id)
                    return 28, 3
            if abs(x - 2211.6) <= abs(y - 508.9):
                if y > 508.9:
                    ji.veh_segement_martix[28][0].append(node_id)
                    return 28, 0
                if y < 508.9:
                    ji.veh_segement_martix[28][2].append(node_id)
                    return 28, 2
        ji.junction_vehicle[29].append(node_id)
        if abs(x - 2559.2) > abs(y - 508.9):
            if x > 2559.2:
                ji.veh_segement_martix[29][1].append(node_id)
                return 29, 1
            if x < 2559.2:
                ji.veh_segement_martix[29][3].append(node_id)
                return 29, 3
        if abs(x - 2559.2) <= abs(y - 508.9):
            if y > 508.9:
                ji.veh_segement_martix[29][0].append(node_id)
                return 29, 0
            if y < 508.9:
                ji.veh_segement_martix[29][2].append(node_id)
                return 29, 2

    if x > 463.3 and y < 684.75:
        if x < 694.05:
            ji.junction_vehicle[22].append(node_id)
            ji.veh_segement_martix[22][0].append(node_id)
            return 22, 0
        if x < 991.1:
            ji.junction_vehicle[23].append(node_id)
            ji.veh_segement_martix[23][0].append(node_id)
            return 23, 0
        if x < 1286.9:
            ji.junction_vehicle[24].append(node_id)
            ji.veh_segement_martix[24][0].append(node_id)
            return 24, 0
        if x < 1514.8:
            ji.junction_vehicle[25].append(node_id)
            ji.veh_segement_martix[25][0].append(node_id)
            return 25, 0
        if x < 1798:
            ji.junction_vehicle[26].append(node_id)
            ji.veh_segement_martix[26][0].append(node_id)
            return 26, 0
        if x < 2086.35:
            ji.junction_vehicle[27].append(node_id)
            ji.veh_segement_martix[27][0].append(node_id)
            return 27, 0
        if x < 2385.4:
            ji.junction_vehicle[28].append(node_id)
            ji.veh_segement_martix[28][0].append(node_id)
            return 28, 0
        ji.junction_vehicle[29].append(node_id)
        ji.veh_segement_martix[29][0].append(node_id)
        return 29, 0

    if y < 766.25:
        if x < 170.9:
            ji.junction_vehicle[30].append(node_id)
            if abs(x - 0) > abs(y - 671.9):
                if x > 0:
                    ji.veh_segement_martix[30][1].append(node_id)
                    return 30, 1
                if x < 0:
                    ji.veh_segement_martix[30][3].append(node_id)
                    return 30, 3
            if abs(x - 0) <= abs(y - 671.9):
                if y > 671.9:
                    ji.veh_segement_martix[30][0].append(node_id)
                    return 30, 0
                if y < 671.9:
                    ji.veh_segement_martix[30][2].append(node_id)
                    return 30, 2
        if x < 463.4:
            ji.junction_vehicle[31].append(node_id)
            if abs(x - 341.8) > abs(y - 671.9):
                if x > 341.8:
                    ji.veh_segement_martix[31][1].append(node_id)
                    return 31, 1
                if x < 341.8:
                    ji.veh_segement_martix[31][3].append(node_id)
                    return 31, 3
            if abs(x - 341.8) <= abs(y - 671.9):
                if y > 671.9:
                    ji.veh_segement_martix[31][0].append(node_id)
                    return 31, 0
                if y < 671.9:
                    ji.veh_segement_martix[31][2].append(node_id)
                    return 31, 2

    if y < 948.9:
        if x < 170.9:
            ji.junction_vehicle[40].append(node_id)
            if abs(x - 0) > abs(y - 1037.2):
                if x > 0:
                    ji.veh_segement_martix[40][1].append(node_id)
                    return 40, 1
                if x < 0:
                    ji.veh_segement_martix[40][3].append(node_id)
                    return 40, 3
            if abs(x - 0) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[40][0].append(node_id)
                    return 40, 0
                if y < 1037.2:
                    ji.veh_segement_martix[40][2].append(node_id)
                    return 40, 2
        if x < 463.4:
            ji.junction_vehicle[41].append(node_id)
            if abs(x - 341.8) > abs(y - 1037.2):
                if x > 341.8:
                    ji.veh_segement_martix[41][1].append(node_id)
                    return 41, 1
                if x < 341.8:
                    ji.veh_segement_martix[41][3].append(node_id)
                    return 41, 3
            if abs(x - 341.8) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[41][0].append(node_id)
                    return 41, 0
                if y < 1037.2:
                    ji.veh_segement_martix[41][2].append(node_id)
                    return 41, 2
        if x < 694.05:
            ji.junction_vehicle[42].append(node_id)
            if abs(x - 585) > abs(y - 1037.2):
                if x > 585:
                    ji.veh_segement_martix[42][1].append(node_id)
                    return 42, 1
                if x < 585:
                    ji.veh_segement_martix[42][3].append(node_id)
                    return 42, 3
            if abs(x - 585) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[42][0].append(node_id)
                    return 42, 0
                if y < 1037.2:
                    ji.veh_segement_martix[42][2].append(node_id)
                    return 42, 2
        if x < 991.1:
            ji.junction_vehicle[43].append(node_id)
            if abs(x - 803.1) > abs(y - 1037.2):
                if x > 803.1:
                    ji.veh_segement_martix[43][1].append(node_id)
                    return 43, 1
                if x < 803.1:
                    ji.veh_segement_martix[43][3].append(node_id)
                    return 43, 3
            if abs(x - 803.1) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[43][0].append(node_id)
                    return 43, 0
                if y < 1037.2:
                    ji.veh_segement_martix[43][2].append(node_id)
                    return 43, 2
        if x < 1286.9:
            ji.junction_vehicle[44].append(node_id)
            if abs(x - 1179.1) > abs(y - 1037.2):
                if x > 1179.1:
                    ji.veh_segement_martix[44][1].append(node_id)
                    return 44, 1
                if x < 1179.1:
                    ji.veh_segement_martix[44][3].append(node_id)
                    return 44, 3
            if abs(x - 1179.1) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[44][0].append(node_id)
                    return 44, 0
                if y < 1037.2:
                    ji.veh_segement_martix[44][2].append(node_id)
                    return 44, 2
        if x < 1514.8:
            ji.junction_vehicle[45].append(node_id)
            if abs(x - 1394.7) > abs(y - 1037.2):
                if x > 1394.7:
                    ji.veh_segement_martix[45][1].append(node_id)
                    return 45, 1
                if x < 1394.7:
                    ji.veh_segement_martix[45][3].append(node_id)
                    return 45, 3
            if abs(x - 1394.7) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[45][0].append(node_id)
                    return 45, 0
                if y < 1037.2:
                    ji.veh_segement_martix[45][2].append(node_id)
                    return 45, 2
        if x < 1798:
            ji.junction_vehicle[46].append(node_id)
            if abs(x - 1634.9) > abs(y - 1037.2):
                if x > 1634.9:
                    ji.veh_segement_martix[46][1].append(node_id)
                    return 46, 1
                if x < 1634.9:
                    ji.veh_segement_martix[46][3].append(node_id)
                    return 46, 3
            if abs(x - 1634.9) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[46][0].append(node_id)
                    return 46, 0
                if y < 1037.2:
                    ji.veh_segement_martix[46][2].append(node_id)
                    return 46, 2
        if x < 2086.35:
            ji.junction_vehicle[47].append(node_id)
            if abs(x - 1961.1) > abs(y - 1037.2):
                if x > 1961.1:
                    ji.veh_segement_martix[47][1].append(node_id)
                    return 47, 1
                if x < 1961.1:
                    ji.veh_segement_martix[47][3].append(node_id)
                    return 47, 3
            if abs(x - 1961.1) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[47][0].append(node_id)
                    return 47, 0
                if y < 1037.2:
                    ji.veh_segement_martix[47][2].append(node_id)
                    return 47, 2
        if x < 2385.4:
            ji.junction_vehicle[48].append(node_id)
            if abs(x - 2211.6) > abs(y - 1037.2):
                if x > 2211.6:
                    ji.veh_segement_martix[48][1].append(node_id)
                    return 48, 1
                if x < 2211.6:
                    ji.veh_segement_martix[48][3].append(node_id)
                    return 48, 3
            if abs(x - 2211.6) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[48][0].append(node_id)
                    return 48, 0
                if y < 1037.2:
                    ji.veh_segement_martix[48][2].append(node_id)
                    return 48, 2
        ji.junction_vehicle[49].append(node_id)
        if abs(x - 2559.2) > abs(y - 1037.2):
            if x > 2559.2:
                ji.veh_segement_martix[49][1].append(node_id)
                return 49, 1
            if x < 2559.2:
                ji.veh_segement_martix[49][3].append(node_id)
                return 49, 3
        if abs(x - 2559.2) <= abs(y - 1037.2):
            if y > 1037.2:
                ji.veh_segement_martix[49][0].append(node_id)
                return 49, 0
            if y < 1037.2:
                ji.veh_segement_martix[49][2].append(node_id)
                return 49, 2

    if y < 1160.95:
        if x < 170.9:
            ji.junction_vehicle[50].append(node_id)
            if abs(x - 0) > abs(y - 1037.2):
                if x > 0:
                    ji.veh_segement_martix[50][1].append(node_id)
                    return 50, 1
                if x < 0:
                    ji.veh_segement_martix[50][3].append(node_id)
                    return 50, 3
            if abs(x - 0) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[50][0].append(node_id)
                    return 50, 0
                if y < 1037.2:
                    ji.veh_segement_martix[50][2].append(node_id)
                    return 50, 2
        if x < 463.4:
            ji.junction_vehicle[51].append(node_id)
            if abs(x - 341.8) > abs(y - 1037.2):
                if x > 341.8:
                    ji.veh_segement_martix[51][1].append(node_id)
                    return 51, 1
                if x < 341.8:
                    ji.veh_segement_martix[51][3].append(node_id)
                    return 51, 3
            if abs(x - 341.8) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[51][0].append(node_id)
                    return 51, 0
                if y < 1037.2:
                    ji.veh_segement_martix[51][2].append(node_id)
                    return 51, 2
        if x < 694.05:
            ji.junction_vehicle[52].append(node_id)
            if abs(x - 585) > abs(y - 1037.2):
                if x > 585:
                    ji.veh_segement_martix[52][1].append(node_id)
                    return 52, 1
                if x < 585:
                    ji.veh_segement_martix[52][3].append(node_id)
                    return 52, 3
            if abs(x - 585) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[52][0].append(node_id)
                    return 52, 0
                if y < 1037.2:
                    ji.veh_segement_martix[52][2].append(node_id)
                    return 52, 2
        if x < 991.1:
            ji.junction_vehicle[53].append(node_id)
            if abs(x - 803.1) > abs(y - 1037.2):
                if x > 803.1:
                    ji.veh_segement_martix[53][1].append(node_id)
                    return 53, 1
                if x < 803.1:
                    ji.veh_segement_martix[53][3].append(node_id)
                    return 53, 3
            if abs(x - 803.1) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[53][0].append(node_id)
                    return 53, 0
                if y < 1037.2:
                    ji.veh_segement_martix[53][2].append(node_id)
                    return 53, 2
        if x < 1286.9:
            ji.junction_vehicle[54].append(node_id)
            if abs(x - 1179.1) > abs(y - 1037.2):
                if x > 1179.1:
                    ji.veh_segement_martix[54][1].append(node_id)
                    return 54, 1
                if x < 1179.1:
                    ji.veh_segement_martix[54][3].append(node_id)
                    return 54, 3
            if abs(x - 1179.1) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[54][0].append(node_id)
                    return 54, 0
                if y < 1037.2:
                    ji.veh_segement_martix[54][2].append(node_id)
                    return 54, 2
        if x < 1514.8:
            ji.junction_vehicle[55].append(node_id)
            if abs(x - 1394.7) > abs(y - 1037.2):
                if x > 1394.7:
                    ji.veh_segement_martix[55][1].append(node_id)
                    return 55, 1
                if x < 1394.7:
                    ji.veh_segement_martix[55][3].append(node_id)
                    return 55, 3
            if abs(x - 1394.7) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[55][0].append(node_id)
                    return 55, 0
                if y < 1037.2:
                    ji.veh_segement_martix[55][2].append(node_id)
                    return 55, 2
        if x < 1798:
            ji.junction_vehicle[56].append(node_id)
            if abs(x - 1634.9) > abs(y - 1037.2):
                if x > 1634.9:
                    ji.veh_segement_martix[56][1].append(node_id)
                    return 56, 1
                if x < 1634.9:
                    ji.veh_segement_martix[56][3].append(node_id)
                    return 56, 3
            if abs(x - 1634.9) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[56][0].append(node_id)
                    return 56, 0
                if y < 1037.2:
                    ji.veh_segement_martix[56][2].append(node_id)
                    return 56, 2
        if x < 2086.35:
            ji.junction_vehicle[57].append(node_id)
            if abs(x - 1961.1) > abs(y - 1037.2):
                if x > 1961.1:
                    ji.veh_segement_martix[57][1].append(node_id)
                    return 57, 1
                if x < 1961.1:
                    ji.veh_segement_martix[57][3].append(node_id)
                    return 57, 3
            if abs(x - 1961.1) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[57][0].append(node_id)
                    return 57, 0
                if y < 1037.2:
                    ji.veh_segement_martix[57][2].append(node_id)
                    return 57, 2
        if x < 2385.4:
            ji.junction_vehicle[58].append(node_id)
            if abs(x - 2211.6) > abs(y - 1037.2):
                if x > 2211.6:
                    ji.veh_segement_martix[58][1].append(node_id)
                    return 58, 1
                if x < 2211.6:
                    ji.veh_segement_martix[58][3].append(node_id)
                    return 58, 3
            if abs(x - 2211.6) <= abs(y - 1037.2):
                if y > 1037.2:
                    ji.veh_segement_martix[58][0].append(node_id)
                    return 58, 0
                if y < 1037.2:
                    ji.veh_segement_martix[58][2].append(node_id)
                    return 58, 2
        ji.junction_vehicle[59].append(node_id)
        if abs(x - 2559.2) > abs(y - 1037.2):
            if x > 2559.2:
                ji.veh_segement_martix[59][1].append(node_id)
                return 59, 1
            if x < 2559.2:
                ji.veh_segement_martix[59][3].append(node_id)
                return 59, 3
        if abs(x - 2559.2) <= abs(y - 1037.2):
            if y > 1037.2:
                ji.veh_segement_martix[59][0].append(node_id)
                return 59, 0
            if y < 1037.2:
                ji.veh_segement_martix[59][2].append(node_id)
                return 59, 2

    if y < 1385.2:
        if x < 170.9:
            ji.junction_vehicle[60].append(node_id)
            if abs(x - 0) > abs(y - 1284.7):
                if x > 0:
                    ji.veh_segement_martix[60][1].append(node_id)
                    return 60, 1
                if x < 0:
                    ji.veh_segement_martix[60][3].append(node_id)
                    return 60, 3
            if abs(x - 0) <= abs(y - 1284.7):
                if y > 1284.7:
                    ji.veh_segement_martix[60][0].append(node_id)
                    return 60, 0
                if y < 1284.7:
                    ji.veh_segement_martix[60][2].append(node_id)
                    return 60, 2
        if x < 578.725:
            ji.junction_vehicle[61].append(node_id)
            if abs(x - 341.8) > abs(y - 1284.7):
                if x > 341.8:
                    ji.veh_segement_martix[61][1].append(node_id)
                    return 61, 1
                if x < 341.8:
                    ji.veh_segement_martix[61][3].append(node_id)
                    return 61, 3
            if abs(x - 341.8) <= abs(y - 1284.7):
                if y > 1284.7:
                    ji.veh_segement_martix[61][0].append(node_id)
                    return 61, 0
                if y < 1284.7:
                    ji.veh_segement_martix[61][2].append(node_id)
                    return 61, 2
        if x < 1139:
            ji.junction_vehicle[63].append(node_id)
            if abs(x - 803.1) > abs(y - 1284.7):
                if x > 803.1:
                    ji.veh_segement_martix[63][1].append(node_id)
                    return 63, 1
                if x < 803.1:
                    ji.veh_segement_martix[63][3].append(node_id)
                    return 63, 3
            if abs(x - 803.1) <= abs(y - 1284.7):
                if y > 1284.7:
                    ji.veh_segement_martix[63][0].append(node_id)
                    return 63, 0
                if y < 1284.7:
                    ji.veh_segement_martix[63][2].append(node_id)
                    return 63, 2
        if x < 1514.8:
            ji.junction_vehicle[65].append(node_id)
            if abs(x - 1394.7) > abs(y - 1284.7):
                if x > 1394.7:
                    ji.veh_segement_martix[65][1].append(node_id)
                    return 65, 1
                if x < 1394.7:
                    ji.veh_segement_martix[65][3].append(node_id)
                    return 65, 3
            if abs(x - 1394.7) <= abs(y - 1284.7):
                if y > 1284.7:
                    ji.veh_segement_martix[65][0].append(node_id)
                    return 65, 0
                if y < 1284.7:
                    ji.veh_segement_martix[65][2].append(node_id)
                    return 65, 2
        if x < 1798:
            ji.junction_vehicle[66].append(node_id)
            if abs(x - 1634.9) > abs(y - 1284.7):
                if x > 1634.9:
                    ji.veh_segement_martix[66][1].append(node_id)
                    return 66, 1
                if x < 1634.9:
                    ji.veh_segement_martix[66][3].append(node_id)
                    return 66, 3
            if abs(x - 1634.9) <= abs(y - 1284.7):
                if y > 1284.7:
                    ji.veh_segement_martix[66][0].append(node_id)
                    return 66, 0
                if y < 1284.7:
                    ji.veh_segement_martix[66][2].append(node_id)
                    return 66, 2
        if x < 2086.35:
            ji.junction_vehicle[67].append(node_id)
            if abs(x - 1961.1) > abs(y - 1284.7):
                if x > 1961.1:
                    ji.veh_segement_martix[67][1].append(node_id)
                    return 67, 1
                if x < 1961.1:
                    ji.veh_segement_martix[67][3].append(node_id)
                    return 67, 3
            if abs(x - 1961.1) <= abs(y - 1284.7):
                if y > 1284.7:
                    ji.veh_segement_martix[67][0].append(node_id)
                    return 67, 0
                if y < 1284.7:
                    ji.veh_segement_martix[67][2].append(node_id)
                    return 67, 2
        if x < 2385.4:
            ji.junction_vehicle[68].append(node_id)
            if abs(x - 2211.6) > abs(y - 1284.7):
                if x > 2211.6:
                    ji.veh_segement_martix[68][1].append(node_id)
                    return 68, 1
                if x < 2211.6:
                    ji.veh_segement_martix[68][3].append(node_id)
                    return 68, 3
            if abs(x - 2211.6) <= abs(y - 1284.7):
                if y > 1284.7:
                    ji.veh_segement_martix[68][0].append(node_id)
                    return 68, 0
                if y < 1284.7:
                    ji.veh_segement_martix[68][2].append(node_id)
                    return 68, 2
        ji.junction_vehicle[69].append(node_id)
        if abs(x - 2559.2) > abs(y - 1284.7):
            if x > 2559.2:
                ji.veh_segement_martix[69][1].append(node_id)
                return 69, 1
            if x < 2559.2:
                ji.veh_segement_martix[69][3].append(node_id)
                return 69, 3
        if abs(x - 2559.2) <= abs(y - 1284.7):
            if y > 1284.7:
                ji.veh_segement_martix[69][0].append(node_id)
                return 69, 0
            if y < 1284.7:
                ji.veh_segement_martix[69][2].append(node_id)
                return 69, 2

    if x < 170.9:
        ji.junction_vehicle[70].append(node_id)
        if abs(x - 0) > abs(y - 1485.7):
            if x > 0:
                ji.veh_segement_martix[70][1].append(node_id)
                return 70, 1
            if x < 0:
                ji.veh_segement_martix[70][3].append(node_id)
                return 70, 3
        if abs(x - 0) <= abs(y - 1485.7):
            if y > 1485.7:
                ji.veh_segement_martix[70][0].append(node_id)
                return 70, 0
            if y < 1485.7:
                ji.veh_segement_martix[70][2].append(node_id)
                return 70, 2
    if x < 578.725:
        ji.junction_vehicle[71].append(node_id)
        if abs(x - 341.8) > abs(y - 1485.7):
            if x > 341.8:
                ji.veh_segement_martix[71][1].append(node_id)
                return 71, 1
            if x < 341.8:
                ji.veh_segement_martix[71][3].append(node_id)
                return 71, 3
        if abs(x - 341.8) <= abs(y - 1485.7):
            if y > 1485.7:
                ji.veh_segement_martix[71][0].append(node_id)
                return 71, 0
            if y < 1485.7:
                ji.veh_segement_martix[71][2].append(node_id)
                return 71, 2
    if x < 1139:
        ji.junction_vehicle[73].append(node_id)
        if abs(x - 803.1) > abs(y - 1485.7):
            if x > 803.1:
                ji.veh_segement_martix[73][1].append(node_id)
                return 73, 1
            if x < 803.1:
                ji.veh_segement_martix[73][3].append(node_id)
                return 73, 3
        if abs(x - 803.1) <= abs(y - 1485.7):
            if y > 1485.7:
                ji.veh_segement_martix[73][0].append(node_id)
                return 73, 0
            if y < 1485.7:
                ji.veh_segement_martix[73][2].append(node_id)
                return 73, 2
    if x < 1656.4:
        ji.junction_vehicle[75].append(node_id)
        if abs(x - 1394.7) > abs(y - 1485.7):
            if x > 1394.7:
                ji.veh_segement_martix[75][1].append(node_id)
                return 75, 1
            if x < 1394.7:
                ji.veh_segement_martix[75][3].append(node_id)
                return 75, 3
        if abs(x - 1394.7) <= abs(y - 1485.7):
            if y > 1485.7:
                ji.veh_segement_martix[75][0].append(node_id)
                return 75, 0
            if y < 1485.7:
                ji.veh_segement_martix[75][2].append(node_id)
                return 75, 2
    if x < 2086.35:
        ji.junction_vehicle[77].append(node_id)
        if abs(x - 1961.1) > abs(y - 1485.7):
            if x > 1961.1:
                ji.veh_segement_martix[77][1].append(node_id)
                return 77, 1
            if x < 1961.1:
                ji.veh_segement_martix[77][3].append(node_id)
                return 77, 3
        if abs(x - 1961.1) <= abs(y - 1485.7):
            if y > 1485.7:
                ji.veh_segement_martix[77][0].append(node_id)
                return 77, 0
            if y < 1485.7:
                ji.veh_segement_martix[77][2].append(node_id)
                return 77, 2
    if x < 2385.4:
        ji.junction_vehicle[78].append(node_id)
        if abs(x - 2211.6) > abs(y - 1485.7):
            if x > 2211.6:
                ji.veh_segement_martix[78][1].append(node_id)
                return 78, 1
            if x < 2211.6:
                ji.veh_segement_martix[78][3].append(node_id)
                return 78, 3
        if abs(x - 2211.6) <= abs(y - 1485.7):
            if y > 1485.7:
                ji.veh_segement_martix[78][0].append(node_id)
                return 78, 0
            if y < 1485.7:
                ji.veh_segement_martix[78][2].append(node_id)
                return 78, 2
    ji.junction_vehicle[79].append(node_id)
    if abs(x - 2559.2) > abs(y - 1485.7):
        if x > 2559.2:
            ji.veh_segement_martix[79][1].append(node_id)
            return 79, 1
        if x < 2559.2:
            ji.veh_segement_martix[79][3].append(node_id)
            return 79, 3
    if abs(x - 2559.2) <= abs(y - 1485.7):
        if y > 1485.7:
            ji.veh_segement_martix[79][0].append(node_id)
            return 79, 0
        if y < 1485.7:
            ji.veh_segement_martix[79][2].append(node_id)
            return 79, 2


def cal_weight(node, next_node, des):
    den_in = 0.0
    h_in = 0.0
    dis_in = 0.0
    if ji.adj_martix[node][next_node] != 0:
        if next_node - node == 1:
            den_in = float((ji.num_segement_martix[node][1] + ji.num_segement_martix[next_node][3])) / float(ji.adj_martix[node][next_node]) * 12.5
        else:
            if next_node - node == -1:
                den_in = float((ji.num_segement_martix[node][3] + ji.num_segement_martix[next_node][1])) / float(ji.adj_martix[node][next_node]) * 12.5
            else:
                if next_node - node == 10:
                    den_in = float((ji.num_segement_martix[node][0] + ji.num_segement_martix[next_node][2]) )/ float(ji.adj_martix[node][next_node]) * 12.5
                else:
                    if next_node - node == -10:
                        den_in = float((ji.num_segement_martix[node][2] + ji.num_segement_martix[next_node][0])) / float(ji.adj_martix[node][next_node]) * 12.5
                    else:
                        if next_node - node == 20:
                            den_in = float((ji.num_segement_martix[node][0] + ji.num_segement_martix[next_node][2])) / float(ji.adj_martix[node][next_node]) * 12.5
                        else:
                            if next_node - node == -20:
                                den_in = float((ji.num_segement_martix[node][2] + ji.num_segement_martix[next_node][0])) / float(ji.adj_martix[node][next_node]) * 12.5
                            else:
                                if next_node - node == 2:
                                    den_in = float((ji.num_segement_martix[node][1] + ji.num_segement_martix[next_node][3])) / float(ji.adj_martix[node][next_node]) * 12.5
                                else:
                                    if next_node - node == -2:
                                        den_in = float((ji.num_segement_martix[node][3] + ji.num_segement_martix[next_node][1])) / float(ji.adj_martix[node][next_node]) * 12.5
        h_in = 0
        dis_in = ji.junction_distance[node][des] - ji.junction_distance[next_node][des] / 100
        if dis_in < 0:
            dis_in = 0
        return den_in, h_in, dis_in
    else:
        return -1, -1, -1


def delete():
    ji.edge_list.clear()
    for i in range(292):
        ji.e_arrival_time[i] = Gp.MAX
    for i in range(80):
        ji.junction_vehicle[i].clear()
        for j in range(4):
            ji.num_segement_martix[i][j] = 0
        for j in range(80):
            ji.chosen_edge[i][j] = 0


def junction_reward(r, des):
    for i in range(80):
        for j in range(80):
            if ji.adj_martix[i][j] != 0:
                a, b, c = cal_weight(i, j, des)
                if a == 0:
                    r[i][j] = 0
                else:
                    r[i][j] = alpha*(a+b) + beta*c
    for i in range(2, 9):
        r[20 + i][30 + i] = 0
        r[30 + i][40 + i] = 0
    r[31][32] = 0
    r[61][62] = 0
    r[62][63] = 0
    r[71][72] = 0
    r[72][73] = 0
    r[63][64] = 0
    r[64][65] = 0
    r[73][74] = 0
    r[74][75] = 0
    r[75][76] = 0
    r[76][77] = 0
    r[des][des] = 1000

def num_count():
    for i in range(80):
        for j in range(4):
            ji.num_segement_martix[i][j] = len(ji.veh_segement_martix[i][j])


def hidden_seq_generate(reward, source, des):
    if source > des:
        flag = 1
    else:
        flag = 0
    g = nx.DiGraph()
    for i in range(80):
        for j in range(80):
            if reward[i][j] != 0:
               g.add_edge(i, j, weight=1000-reward[i][j])
    # a = nx.shortest_path(g,source=source,target=des)
    a = dij.Dijkstra(g, source, des)
    print("intersection1:")
    print(a)
    if(a!=None):
        for i in range(len(a)-1):
            ji.chosen_edge[a[i]][a[i+1]] = 1
            g.remove_edge(a[i], a[i+1])
    # b = nx.shortest_path(g, source=source, target=des)
    b = dij.Dijkstra(g, source, des)
    # if flag == 0:
    #     for i in range(len(b) - 1):
    #         ji.chosen_edge[b[i]][b[i + 1]] = 1
    #         for j in range(len(a)):
    #             if reward[b[i]][a[j]] != -1 and a[j] > b[i]:
    #                 ji.chosen_edge[b[i]][a[j]] = 1
    # else:
    #     for i in range(len(b) - 1):
    #         ji.chosen_edge[b[i]][b[i + 1]] = 1
    #         for j in range(len(a)):
    #             if reward[b[i]][a[j]] != -1 and a[j] < b[i]:
    #                 ji.chosen_edge[b[i]][a[j]] = 1
    print("intersection2:")
    print(b)
    return a, b
    # if source == des or time > 15:
    #     return
    # sum = 0
    # num = 0
    # if (source + 1 < 80 and reward[source][source + 1] != -1):
    #     sum += reward[source][source + 1]
    #     num.append(node_id)
    # if (source - 1 >=0 and reward[source][source - 1] != -1):
    #     sum += reward[source][source - 1]
    #     num.append(node_id)
    # if (source + 10 < 80 and reward[source][source + 10] != -1):
    #     sum += reward[source][source + 10]
    #     num.append(node_id)
    # if (source - 10 >= 0 and reward[source][source - 10] != -1):
    #     sum += reward[source][source - 10]
    #     num.append(node_id)
    # if (source + 20 < 80 and reward[source][source + 20] != -1):
    #     sum += reward[source][source + 20]
    #     num.append(node_id)
    # if (source - 20 >= 0 and reward[source][source - 20] != -1):
    #     sum += reward[source][source - 20]
    #     num.append(node_id)
    # if (source + 2 < 80 and reward[source][source + 2] != -1):
    #     sum += reward[source][source + 2]
    #     num.append(node_id)
    # if (source - 2 >= 0 and reward[source][source - 2] != -1):
    #     sum += reward[source][source - 2]
    #     num.append(node_id)
    # ave = (sum / num) * 1.2
    # if (source + 1 < 80 and reward[source][source + 1] != -1 and reward[source][source + 1] >= ave):
    #     self.chosen_edge[source][source+1] = 1
    #     self.hidden_seq_generate(reward, source+1, des, time + 1)
    #
    # if (source - 1 >=0 and reward[source][source - 1] != -1 and reward[source][source - 1] >= ave):
    #     self.chosen_edge[source][source - 1] = 1
    #     self.hidden_seq_generate(reward, source - 1, des, time + 1)
    #
    # if (source + 10 < 80 and reward[source][source + 10] != -1 and reward[source][source + 10] >= ave):
    #     self.chosen_edge[source][source + 10] = 1
    #     self.hidden_seq_generate(reward, source + 10, des, time + 1)
    #
    # if (source - 10 >= 0 and reward[source][source - 10] != -1 and reward[source][source - 10] >= ave):
    #     self.chosen_edge[source][source - 10] = 1
    #     self.hidden_seq_generate(reward, source - 10, des, time + 1)
    #
    # if (source + 20 < 80 and reward[source][source + 20] != -1 and reward[source][source + 20] >= ave):
    #     self.chosen_edge[source][source + 20] = 1
    #     self.hidden_seq_generate(reward, source + 20, des, time + 1)
    #
    # if (source - 20 >= 0 and reward[source][source - 20] != -1 and reward[source][source - 20] >= ave):
    #     self.chosen_edge[source][source - 20] = 1
    #     self.hidden_seq_generate(reward, source - 20, des, time + 1)
    #
    # if (source + 2 < 80 and reward[source][source + 2] != -1 and reward[source][source + 2] >= ave):
    #     self.chosen_edge[source][source+2] = 1
    #     self.hidden_seq_generate(reward, source+2, des, time + 1)
    #
    # if (source - 2 >= 0 and reward[source][source - 2] != -1 and reward[source][source - 2] >= ave):
    #     self.chosen_edge[source][source - 2] = 1
    #     self.hidden_seq_generate(reward, source - 2, des, time + 1)
    # return

def cal_dis(i, j, node_list):
    return pow(node_list[i].position[0] - node_list[j].position[0], 2) + pow(node_list[i].position[1] - node_list[j].position[1], 2)

def hidden_to_obverse(source_vehicle, des_vehicle, node_list, hidden_seq):
    if hidden_seq is None:
        return
    for i in range(len(hidden_seq)-1):
        if i == 0:
            for nodei in ji.junction_vehicle[hidden_seq[i + 1]]:
                node = int(nodei)
                d = cal_dis(source_vehicle, node, node_list)
                if d < pow(Gp.com_dis, 2):
                    insort_right(ji.edge_list, edge(source_vehicle, node, ji.e_arrival_time[source_vehicle], d))
                    if ji.e_arrival_time[node] > (ji.e_arrival_time[source_vehicle] + d):
                        ji.e_arrival_time[node] = ji.e_arrival_time[source_vehicle] + d
        else:
            if i == len(hidden_seq)-1:
                for nodei in ji.junction_vehicle[hidden_seq[i]]:
                    node = int(nodei)
                    d = cal_dis(des_vehicle, node, node_list)
                    if d < pow(Gp.com_dis, 2):
                        insort_right(ji.edge_list, edge(node, des_vehicle, ji.e_arrival_time[node], d))
                        if ji.e_arrival_time[des_vehicle] > (ji.e_arrival_time[node] + d):
                            ji.e_arrival_time[des_vehicle] = ji.e_arrival_time[node] + d
            else:
                for s_nodei in ji.junction_vehicle[hidden_seq[i]]:
                    s_node = int(s_nodei)
                    for d_nodei in ji.junction_vehicle[hidden_seq[i+1]]:
                        d_node = int(d_nodei)
                        d = cal_dis(s_node, d_node, node_list)
                        if d < pow(Gp.com_dis, 2):
                            insort_right(ji.edge_list, edge(s_node, d_node, ji.e_arrival_time[s_node], d))
                            if ji.e_arrival_time[d_node] > (ji.e_arrival_time[s_node] + d):
                                ji.e_arrival_time[d_node] = ji.e_arrival_time[s_node] + d


def hidden_to_obverse_1(source, des, node_list, main_seq, sub_seq):
    if main_seq is None or sub_seq is None:
        return
    if node_list[des].junction[0] > node_list[source].junction[0]:
        flag = 1
    else:
        flag = 0
    for sub in sub_seq:
        for main in main_seq:
            if flag == 1:
                if main > sub and ji.adj_martix[sub][main] != 0:
                    for s_node in ji.junction_vehicle[sub]:
                        for d_node in ji.junction_vehicle[main]:
                            if pow(node_list[d_node].position[0] - node_list[s_node].position[0], 2) + pow(
                                    node_list[d_node].position[1] - node_list[s_node].position[1], 2) < pow(Gp.com_dis,
                                                                                                            2):
                                insort_right(ji.edge_list, edge(s_node, d_node, ji.e_arrival_time[s_node], 1))
                                if ji.e_arrival_time[d_node] > (ji.e_arrival_time[s_node] + 1):
                                    ji.e_arrival_time[d_node] = ji.e_arrival_time[s_node] + 1
            else:
                if main < sub and ji.adj_martix[sub][main] != 0:
                    for s_node in ji.junction_vehicle[sub]:
                        for d_node in ji.junction_vehicle[main]:
                            if pow(node_list[d_node].position[0] - node_list[s_node].position[0], 2) + pow(
                                    node_list[d_node].position[1] - node_list[s_node].position[1], 2) < pow(Gp.com_dis,
                                                                                                            2):
                                insort_right(ji.edge_list, edge(s_node, d_node, ji.e_arrival_time[s_node], 1))
                                if ji.e_arrival_time[d_node] > (ji.e_arrival_time[s_node] + 1):
                                    ji.e_arrival_time[d_node] = ji.e_arrival_time[s_node] + 1





    # for i in range(80):
    #     if ji.chosen_edge[node_list[source_vehicle].junction[0]][i] == 1:
    #         for j in ji.junction_vehicle[i]:
    #             if pow(node_list[j].position[0] - node_list[source_vehicle].position[0], 2) + pow(node_list[j].position[1] - node_list[source_vehicle].position[1], 2) < pow(Gp.com_dis, 2):
    #                 insort_right(ji.edge_list, edge(source_vehicle, j, ji.e_arrival_time[source_vehicle], 1))
    #                 if ji.e_arrival_time[j] > (ji.e_arrival_time[source_vehicle] + 1):
    #                     ji.e_arrival_time[j] = ji.e_arrival_time[source_vehicle] + 1
    #                 hidden_to_obverse(j, des_vehicle, node_list)

