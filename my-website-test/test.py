from flask import Flask

app = Flask(__name__)

@app.route("/hello")
def hello():
    return "这是 Python 传回来的内容！"

if __name__ == "__main__":
    app.run(debug=True)