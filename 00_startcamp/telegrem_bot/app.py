from flask import Flask, render_template, request
import requests
from decouple import config


app = Flask(__name__)
api_url = 'https://api.telegram.org'
token = config('TELEGRAM_BOT_TOKEN')
chat_id = config('CHAT_ID')
naver_client_id = config('NAVER_CLIENT_ID')
naver_client_secert = config('NAVER_CLIENT_SECRET')

@app.route('/')
def hello():
    return 'Hi there!'

# @app.route('/write')
# def write():
#     return render_template('write.html')

# @app.route('/send')
# def send():
#     text = request.args.get('message')

#     requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}')
#     return render_template('send.html')

@app.route(f'/{token}', methods =['POST'])
def telegram():
    #step 1. 데이터 구조 print해보기
    from_telegrem = request.get_json()

    if from_telegrem.get('message') is not None:
    #step 2. 그대로 돌려보내기
        chat_id = from_telegrem.get('message').get('from').get('id')
        text = from_telegrem.get('message').get('text')
     
    #한글 키워드 받기

        #'/번역 '으로 입력이 시작한다면, 파파고로 번역이 동작한다
        if text[0:4] == '/번역 ':
            headers = {
                'X-Naver-Client-Id' : naver_client_id,
                'X-Naver-Client-Secret' : naver_client_secert
            }
            data = {'source' : 'ko', 'target' : 'en', 'text' : text[4:]}
            papago_res = requests.post('https://openapi.naver.com/v1/papago/n2mt', headers=headers, data=data)
            text = papago_res.json().get('message').get('result').get('translatedText') #여기에 한/영 번역 텍스트가있음

        if text[0:4] == '/로또 ':
            num = text[4:]
            res = requests.get(f'https://www.dhlottery.co.kr/common.do?method=getLottoNumber&drwNo={num}')
            lotto = res.json()
            winner = []
            for i in range(1,7):
                winner.append(lotto[f'drwtNo{i}'])
            bonus_num = lotto['bnusNo']
            text= f'로또 {num}회차 {winner} + {bonus_num} 입니다.'
        requests.get(f'{api_url}/bot{token}/sendMessage?chat_id={chat_id}&text={text}') #메아리

        
    #한글 키워드 받기
    return '', 200

