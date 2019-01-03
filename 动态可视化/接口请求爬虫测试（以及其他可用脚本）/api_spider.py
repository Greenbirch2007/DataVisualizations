


import requests


def call_api(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text

    else:
        return '<h1>请求有问题</h1>'


url = 'http://127.0.0.1:5000/data'
html = call_api(url)
print(html)


