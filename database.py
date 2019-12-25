#-*-coding:utf-8-*-
import pachong
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["html"] #集合
result = mycol.delete_many({})  # 清空数据库，重新开始爬取数据
x = mycol.insert_many(pachong.all_data)
