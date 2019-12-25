#-*-coding:utf-8-*-
import re
import requests
from bs4 import BeautifulSoup
url='http://news.bjfu.edu.cn/lsxy/'
all_url_list=[]#用来存放所用的url
all_data=[]
def getdetail(url):#获取详细的信息
    resd =requests.get(url)
    resd.encoding='GBK'
    soupd=BeautifulSoup(resd.text,'html.parser')
    return (soupd.select('.article')[0])
def get_all_url():
    #第一访问绿色要闻的第一页
    res = requests.get(url)
    res.encoding = 'GBK'
    soup = BeautifulSoup(res.text, 'html.parser')
    for news in soup.select('.list_conr li'):
        detailUrl = news.select("a")[0]['href']
        all_url_list.append(url+detailUrl)
        print("爬取到链接：",url+detailUrl)
    #访问绿色新闻网的剩余1-41页，并把页面中的新闻url添加到all_url_list中
    for i in range(1,42):
        nexturl=url+'index'+str(i)+'.html'
        res = requests.get(nexturl)
        res.encoding = 'GBK'
        soup = BeautifulSoup(res.text, 'html.parser')
        for news in soup.select('.list_conr li'):
            detailUrl = news.select("a")[0]['href']
            if (detailUrl[0:4]=='http'):continue
            all_url_list.append(url + detailUrl)
            print("爬取到链接：", url + detailUrl)
    print("爬取完毕，共",len(all_url_list),'个链接')
def  analyse_new(url):
    requestsoup=getdetail(url)
    dict={}
    newsTitle = requestsoup.select("h2")[0].text#获取文本标题
    newsPublishTime = requestsoup.select("span")[0].text#获取时间
    newsClickCount=requestsoup.select("div")[4].select('script')[0]['src']#获取点击次数开始
    res3=requests.get("http://news.bjfu.edu.cn/"+newsClickCount)
    newsClickCount = BeautifulSoup(res3.text, 'html.parser').text
    newsClickCount=eval(re.findall(r'[(](.*?)[)]', newsClickCount)[0])#获取点击次数结束
    newsSource=requestsoup.select("div")[4].select("span")[0].text#获取部门来源
    newsContent=requestsoup.select(".article_con")[0].text#获取新闻内容
    dict['id']=url
    dict['newsTitle']=newsTitle
    dict['newsContent']=newsContent
    dict['newsPublishTime']=newsPublishTime
    dict['newsClickCount']=newsClickCount
    dict['newsSource']=newsSource
    all_data.append(dict)
def pachongMain():
    get_all_url()
    print("正在存入数据，请稍等....")
    for url in all_url_list:
        analyse_new(url)
pachongMain()