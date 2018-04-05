from flask import Flask, render_template
app = Flask(__name__,static_url_path='')

@app.route('/')
def index():
    # return render_template('请访问http://127.0.0.1:8808/reprot/index.html')
    return '<h1>请访问http://127.0.0.1:8808/reprot/index.html</h1>'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8808, debug=True)
