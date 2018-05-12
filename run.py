# -*- coding:utf-8 -*-
__author__ = 'nahsor'
from flask_cors import CORS
from app import create_app
from app.response import products, projects, modules, testcass

app = create_app("ProductionConfig")
CORS(app)

@app.route('/')
def index():
    # return '<h1>请访问http://127.0.0.1:8808/report/index.html</h1>'
    return app.send_static_file('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8808, threaded=True)
