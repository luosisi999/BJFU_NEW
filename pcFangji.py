#-*-coding:utf-8-*-
import re
import os
import ast
import json
import requests
from bs4 import BeautifulSoup
url='http://tcm.med.wanfangdata.com.cn/Resource/AjaxGetCategories?dbName=MedTCMFangJi&categoryParams=%7CCategoryFirst=%E7%9C%BC%E7%A7%91%E7%94%A8%E8%8D%AF&pageIndex='
all_data=[]
d_data=[]
def getdetail(url):#获取详细的信息
    print("爬取网址:",url)
    resd =requests.get(url)
    resd.encoding='utf-8'
    soupd=BeautifulSoup(resd.text,'html.parser')
    str1=str(soupd)
    dict = json.loads(str1)
    print("爬取到的数据：",dict)
    all_data.append(dict)
for i in range(1,50):
    url1=url+str(i)
    getdetail(url1)
length=len(all_data)
data=[]
for l in all_data:
    lists=l.get('categoriesList')
    lists = ast.literal_eval(lists)
    for j in lists:
        data.append(j.get('Value'))
print(data)


# 以写的方式打开文件，如果文件不存在，就会自动创建
file_write_obj = open("dest.txt", 'w',encoding='utf-8')
for var in data:
  file_write_obj.writelines(var)
  file_write_obj.write('\n')
file_write_obj.close()


