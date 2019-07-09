import requests
from bs4 import BeautifulSoup

html = requests.get('https://www.naver.com/').text
#만약 현재변수 html(url)이 길다면 따로 변수로 지정하여 코드를 간략하게 정리함
soup = BeautifulSoup(html, 'html.parser')
search = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_k')
rank = soup.select('#PM_ID_ct > div.header > div.section_navbar > div.area_hotkeyword.PM_CL_realtimeKeyword_base > div.ah_list.PM_CL_realtimeKeyword_list_base > ul > li > a.ah_a > span.ah_r')
j=0


for i in search:    
     search_text = i.text
     rank_text = rank[j].text
     j= j+1
     print('현재 검색어 ' + rank_text + '위 ' + search_text )




