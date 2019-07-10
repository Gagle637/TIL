import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.naver.com/').text
# 요청 보내서 html 파일 받고
soup = BeautifulSoup(html, 'html.parser')
# 뷰티풀수프로 정제
searchs = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')
rank = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_r')
#select 매서드로 사용해서 list를 얻어낸다.
num = range(0,len(searchs)) 
# 범위설정
# print(num)

#뽑은 리스트를 with 구문으로 잘 작성해보자

with open('naver_rank.txt', 'w', encoding='utf-8') as f:
    for i in num:
        f.writelines(f' {rank[i].text}. {searchs[i].text} \n')