from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello(): #함수 만드는거 def는 함수실행 return은 값실행 
    return 'This is SSAFY!'  
    
@app.route('/ssafy/') #  /추가주소/  의 방식으로 주소를 바꿈
def hllo():  #겹치면 오류남
    return 'This is SSAFY!'


