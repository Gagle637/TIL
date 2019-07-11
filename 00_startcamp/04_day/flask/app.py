from flask import Flask, render_template, request
from datetime import datetime
import random
app = Flask(__name__)

#render template (변경함)
@app.route('/')
def hello():
    # return 'Hello World!'
    return render_template('index.html')
#app.py 와 같은 위치애 templates(폴더)안에 템플릿 생성

@app.route('/ssafy/')
def ssafy():
    # return 'This is SSAFY!'
    return render_template('ssafy.html')


@app.route('/dday')
def dday():
    # 오늘 날짜
    today_time = datetime.now()
    # 수료 날짜
    endgame = datetime(2019, 11, 29)
    # 수료 날짜 - 오늘 날짜
    dday = endgame - today_time
    # return f'{dday.days} 일 남았습니다.'
    return render_template('dday.html', html_dday=dday.days)


@app.route('/html')
def html():
    return '<h1>This is HTML TAG<h1>'


@app.route('/html_line')
def html_line():
    return """
    <h1>여러줄을 보내봅시다.</h1>
    번호가 없는 리스트를 보냅니다.
     <ul>
     <li> 번호가 없는 리스트</li>
     <li> 번호가 없는 리스트2</li>
     </ul>
    """

#variable routing

@app.route('/greeting/<name>')
# @app.route('/greeting/<string:name>')  #스트링은 생략이 가능하다.
def greeting(name):
    # return f'반갑습니다! {name}!'
    return render_template('greeting.html', html_name=name)


@app.route('/cube/<int:number>')
def cube(number):
    #연산을 모두 끝내고 변수만 cube.html로 넘긴다.
    n_3 = number**3
    # return f'{number}의 세제곱은 {number**3}입니다.'
    return render_template('cube.html',html_n_3=n_3)
#주소의 number의 숫자는 str의 형태로 들어오게 됩니다.
#계산을 위해 int로 변환시키는 과정이 필요합니다.

#lunch/몇명이 식사하는지 인원
#플라스크는 여러 메뉴중에서 인원 수만큼의 메뉴를 응답합니다.

@app.route('/lunch/<int:lunch_people>')
def lunch(lunch_people):
    menus= ['순두부찌게', '오므라이스', '돈까스', '함박스테이크']
    # L_menu=random.sample(menus,lunch_people)
    # return str(L_menu)
    L_menu=random.choices(menus,k=lunch_people)
    return render_template('lunch.html',html_L_menu=L_menu,)

@app.route('/movie')
def movie():
    movies = ['토이스토리4', '스파이더맨', '알라딘', '기생충','엔드게임']
    return render_template('movie.html', movies=movies)


@app.route('/ping')
def ping():
    return render_template('ping.html')

@app.route('/pong')
def pong():
    name = request.args.get('data')  #안녕하세요
    return render_template('pong.html', name=name)


@app.route('/naver')
def naver():
    return render_template('naver.html')

@app.route('/google')
def google():
    return render_template('google.html')

@app.route('/vonvon')
def von():
    return render_template('vonvon.html')

@app.route('/vonvon_result')
def von_result():
    name = request.args.get('name')
    result = ['성격A를', '성격B를', '성격C를', '성격D를', '성격E를', '성격F를', '성격G를', '성격H를', '성격I를', '성격J를']
    last = random.sample(result, 3)
    ABC = [' 한 스ㅍ 으아아아...', ' 한 스푼']
    ASD = random.choices(ABC, k=3)
    return render_template('vonvon_result.html',name=name,last=last,ASD=ASD)