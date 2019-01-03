#! -*- coding:utf-8 -*-

from flask import Flask,request,render_template,jsonify

from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)
# 用了两种路由创建的方法
class DataVis_(Resource):
    def get(self):
        return {'data':[0.13,0.09,0.11,0.08,0.16]}

api.add_resource(DataVis_,'/data')   # 1.接口路由
@app.route('/')  # ２．首页路由
def first_page():
    return '<h1>这是可视化测试首页</h1>'


@app.route('/dv',methods=['GET'])
def data_Show():
    return render_template('index.html')  #3. 视图函数加载



@app.route('/test',methods=['GET'])
def test():
    return render_template('test.html')

if __name__ =='__main__':
    app.run(debug=True)

