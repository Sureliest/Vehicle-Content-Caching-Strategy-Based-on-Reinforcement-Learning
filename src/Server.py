import numpy
import random
import init_data_file as idf
#BS,服务器，如果车辆从附近的rsu获取不到想要的信息，那么附最近的服务器会提供给信息，服务器存有所有的信息
class BS:
    def __init__(self):
        self.file = [] #服务器上存储全部信息
        self.hello_list = [] #获取信息的请求表
        self.content = []
        self.position_x = 0
        self.position_y = 0

    def send_hello_list(self,nodelist):
        for list in self.hello_list:
            pass

    def geo_hello_list(self,node_list):
        pass

    def get_file_list(self):
        file = idf.DataFile()
        movies = file.read_file()
        for movie in movies:
            self.file.append(movie)

    def alt_position(self, x , y):
        self.position_x = x
        self.position_y = y

#RSU,小型存储服务器，用来存储附近车辆最近的信息
class RSU(BS):
    def __init__(self,id):
        BS.__init__(self)
        self.capacity = 20 #rsu服务节点能力
        self.veihcle = [] #当前rsu正在服务的节点
        self.id = id

    def get_file_list(self):
        file = idf.DataFile()
        movies = file.read_file()
        file_num = random.sample(range(0,644),200)
        for i in file_num:
            self.file.append(movies[i])

    def no_kind_file(self):
        base_sever = BS()
        file_list = base_sever.get_file_list()
        print(file_list)


class MBS(BS):

    def __init__(self):
        BS.__init__(self)
        self.movie_type = {}

    def get_file_list(self):
        file = idf.DataFile()
        movies = file.read_file()
        for movie in movies:
            self.file.append(movie)
        self.content_classify()


    def content_classify(self):
        i = 0
        movie_type = []
        for file in self.file:
            # print(file[2])
            # if file[2] == ' ':
            #     movie_type = file[0:2]
            # else:movie_type = file[0:3]
            movie_type = file[0:2]
            if movie_type not in self.movie_type.keys():
                self.movie_type[movie_type] = i
            i += 1



#BS只有一个，而RSU多个
def gen_rsu():
    rsu_list = []
    for i in range(500):
        rsu = RSU(i)
        rsu.get_file_list()
        rsu_list.append(rsu)
    return rsu_list

if __name__ == '__main__':
    mbs = MBS()
    mbs.get_file_list()
    print(mbs.movie_type)
