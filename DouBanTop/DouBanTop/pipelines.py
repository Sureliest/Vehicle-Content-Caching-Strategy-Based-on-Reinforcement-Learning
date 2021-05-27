# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class DoubantopPipeline:
    fp=None
    #重写父类方法
    def open_spider(self,spider):#只会调用一次
        print("starting...")
        self.fp=open('./data.txt','w',encoding='utf-8')
    def process_item(self, item, spider):#每次接受item都会调用一次
        rank = item['rank']
        title = item['title']
        release_date = item['release_date']
        regions = item['regions']
        score = item['score']
        type = item['type']
        self.fp.write(type + " " + str(rank) + ":" + title + " " + release_date+ " " + regions+ " " + str(score) + "\n")
        return item #return操作返回item会传递给下一个即将被执行的管道类
    def close_spider(self,spider):#只会调用一次
        print("exiting.....")
        self.fp.close()
