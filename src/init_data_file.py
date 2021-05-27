import random
import numpy as np
# import Node
#随机生成文件，数据为分类的电影
class DataFile():
    def __init__(self):

        # self.file_path = '../data/data.txt'
        self.file_path = 'D:\Project\python\DEMO\data\data.txt'
        self.file_num = 20
        self.vechile_num = 1

    def vel_num(self):
        return self.vechile_num


    def gen_file(self):
        vehicle_node = []
        files = []
        for i in range(self.vechile_num):
            nodes = random.randint(0,196)
            vehicle_node.append(nodes)
            # file_node = random.sample(range(0,644),self.file_num)
            file_node = zipf()
            files.append(file_node)
        # print(vehicle_node,files)
        return vehicle_node,files

    def read_file(self):
        movies = []
        with open(self.file_path,encoding = 'utf-8') as f:
            for line in f.readlines():
                line = line.strip('\n')
                line = line.split(' ')
                if line[1][2] == ':':
                    movies.append(line[0]+' '+line[1][3::])
                else:movies.append(line[0]+' '+line[1][2::])
        return movies




def zipf():
    k = 13
    s = 1
    p = [0,49,99,149,199,249,299,349,399,449,499,549,599,644]
    f = random.sample(range(1,14),13)
    i = 0
    top = 0
    for rank in f:
        if rank == 1:
            top = i
        else: i += 1
    list = []
    for i in range(20):
        a = 0
        num = random.randint(0,9)
        if num < 8:
            a = random.randint(p[top],p[top+1])
        else:
            a = random.randint(0,644)
        # print(a)
        list.append(a)
    return list



def poission():
    list = np.random.binomial(n=10, p=0.2, size=20)
    print(list)

if __name__ == '__main__':
    for i in range(195):
        print('node:{0}'.format(i))
        a = zipf()
        print(len(a),a)
        file_node = random.sample(range(0, 644), 20)
        print(len(file_node),file_node)
    # print(a)