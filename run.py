from flask import Flask, render_template
app = Flask(__name__,static_url_path='')

@app.route('/')
def index():
	return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8808, debug=True)
