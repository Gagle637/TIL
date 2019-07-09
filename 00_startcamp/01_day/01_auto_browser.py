# import webbrowser
# # 1. 리스트 생성
# # inters = {'www.naver.com', 'www.google.com', 'www.daum.net'}

# url ='https://search.naver.com/search.naver?query='
# idols = {'bts', 'nrg', 'hot','babyvox'}

# # 2. 반복문(for) webbrowser.open()이 실행됨

# for idol in idols:
#    webbrowser.open_new(url + idol)


import requests

response = requests.get('https://www.naver.com/').status_code
print(response)