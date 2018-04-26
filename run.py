# -*- coding:utf-8 -*-
__author__ = 'nahsor'
from app import create_app
from app.response import servers

app = create_app("DevelopmentConfig")


@app.route('/')
def index():
    # return '<h1>请访问http://127.0.0.1:8808/report/index.html</h1>'
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(port=8808)