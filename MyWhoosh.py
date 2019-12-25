#-*-coding:utf-8-*-
from whoosh.qparser import QueryParser
from whoosh.index import create_in
from whoosh.index import open_dir
from whoosh.fields import *
from jieba.analyse import ChineseAnalyzer
from whoosh.sorting import FieldFacet
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["html"]
analyser = ChineseAnalyzer()    #导入中文分词工具
schema = Schema(newTitle=TEXT(stored=True, analyzer=analyser), newContent=TEXT(stored=True, analyzer=analyser),
                    NewId=ID(stored=True))  # 创建索引结构
wh = create_in("./data", schema=schema, indexname='Myindex')  # path 为索引创建的地址，indexname为索引名称
writer = wh.writer()
for x in mycol.find():
    writer.delete_by_term("id", x['id'])  # 为了保证唯一性，先尝试将就path数据删除
    writer.add_document(NewId=x['id'], newTitle=x['newsTitle'], newContent=x['newsContent'])  # 此处为添加的内容
writer.commit()
def find(text):
    ret_list = []
    index = open_dir("./data", indexname='Myindex')  # 读取建立好的索引
    with index.searcher() as searcher:
        parser = QueryParser("newContent", index.schema)
        try:
            word = parser.parse(text)
        except:
            word = None
        if word is not None:
            hits = searcher.search(word, limit=None)
            for hit in hits:
                ret_list.append(dict(hit))
        return ret_list
