

from flask import Flask,render_template,jsonify
from dataConfig import data

app = Flask(__name__)



@app.route('/data') # 数据必须同时考虑x轴和y轴
def api():
    return jsonify({"name":"Greenbirch2007",
                    "id":'000001',
                    "data":data})    #　需要特别序列化
    # return render_template('myapi.html')

@app.route('/api')
def showapi():
    return render_template('index.html')



@app.route('/per')
def percent():
    return render_template('percent.html')

@app.route('/mapi')
def my_api():
    return render_template('myapi.html')

@app.route('/random')
def forever_random():
    return render_template('random.html')

@app.route('/readjson')
def read_jsonDoc():
    return render_template('read_json.html')

if __name__ == '__main__':
    app.run(debug=True)