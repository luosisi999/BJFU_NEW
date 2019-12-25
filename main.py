#-*-coding:utf-8-*-
# import database  #数据库创建成功后可注销
import MyWhoosh
import flask,json
from flask import request
server = flask.Flask(__name__,static_url_path='')
@server.route('/')
def home():
    return server.send_static_file('./index.html')#index.html在static文件夹下
@server.route('/search',methods=['get','post'])
def search():
    searchKey = request.values.get('searchKey')
    result =MyWhoosh.find(searchKey)
    print(result)
    return json.dumps(result, ensure_ascii=False)
if __name__ == '__main__':
    server.run(debug=True, port=80, host='0.0.0.0')

