from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    return 'hi'


app.run(debug=True)  # debug=True 는 code 변경시 자동으로 변경되어 실행됨
# app.run(port=5001, debug=True)  # port 변경이 가능함