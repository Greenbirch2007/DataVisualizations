

from flask import Flask,render_template,jsonify


app = Flask(__name__)



@app.route('/data')
def api():
    return jsonify([{'title':'tst','data':[12908, 5948, 8105, 11248, 8989, 11816, 18274, 18111]}]) #　需要特别序列化

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