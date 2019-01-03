

from flask import Flask,render_template,jsonify


app = Flask(__name__)



@app.route('/data') # 数据必须同时考虑x轴和y轴
def api():
    return jsonify({"name":"Greenbirch2007",
                    "id":'000001',
                    "data":[[1,135],[2,136],[3,137],[4,133],[5,136],[6,169]]})#　需要特别序列化

@app.route('/api')
def showapi():
    return render_template('index.html')

@app.route('/random')
def randomD():
    return render_template('random.html')

@app.route('/per')
def percent():
    return render_template('percent.html')

@app.route('/mapi')
def my_api():
    return "<h1> my api test~</h1>"
    # return render_template('myapi.html')


if __name__ == '__main__':
    app.run(debug=True)