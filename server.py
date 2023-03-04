from flask import Flask
import random

app = Flask(__name__)


@app.route('/')
def index():
    return 'Welcome'


@app.route('/create/')
def create():
    return 'Create'


@app.route('/read/<int:id>/')  # variable한 정보를 보낼경우
def read(id):
    print(id)
    return 'Read '+str(id)

app.run(debug=True)  # debug=True 는 code 변경시 자동으로 변경되어 실행됨
# app.run(port=5001, debug=True)  # port 변경이 가능함