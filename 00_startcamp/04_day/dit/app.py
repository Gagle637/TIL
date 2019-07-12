import requests
from flask import Flask, render_template, request


#로또 회차/내번호 입력 페이지
#결과페이지

app = Flask(__name__)

@app.route('/lotto_check')
def lotto_check():
    return render_template('lotto_check.html')

@app.route('/lotto_result')
def lotto_result():
    #회차번호 받아옴
    num = request.args.get('num')
    #동행복권 요청을 보내 응답을 받는다.
    res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
    #제이슨형태로 변환해준다. (크롬에서 보고있는 결과와 동일한모습)
    lotto = res.json()
    winner = []
    #당첨번호 6개 가져오기
    for i in range(1,7):
        winner.append(lotto[f'drwtNo{i}'])
    #내번호 리스트 만들기
    numbers = []
    for num in request.args.get('numbers').split():
        numbers.append(int(num))
    #등수가리기(몇개 맞았는지 교집합 필요함)
    meched = 0
    #내 번호 리스트를 돌면서/ 뽑은 번호 하나하나가 각각 winner 리스트에 있는지 확인
    # mached = len(set(winner) & set(numbers))
    if len(numbers) == 6:        
        for num in numbers:
            if num in winner:
                meched += 1
        if meched == 6:
            result = '1등입니다.'
        elif meched == 5:
            #보너스 번호가 내 번호안에있을때 2등 아니면 3등
            if lotto['bnusNo'] in numbers:
                result = '2등입니다.'
            else:
                result ='3등입니다.'
        elif meched == 4:
            result = '4등입니다.'
        elif meched == 3:
            result = '5등입니다.'
        else:
            result = '꽝입니다.'
    else:
        result = '번호의 수가 6개가 아닙니다.'

    return render_template('lotto_result.html', winner=winner, numbers=numbers, result=result)


    


        

