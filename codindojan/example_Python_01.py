# 다음 소스 코드를 완성하여 입력된 날짜와 시간을 년-월-일T시:분:초:로 출력하세요

#input 2017 10 277 11 43 59
#Output 2017-10-27T11:43:59

# year, month, day, hour, minute, second =map(int, input().split(' '))
# print(year, month, day, sep = '-',end = 'T')
# print(hour, minute, second, sep=':')


# 국어 90점 이상, 영어는 80점 초과, 수학은 85점 초과, 과학은 80점이상일때 합격이라고 정했습니다.(하나라도 만족하지 못하면 불합격) 합격이면 True 불합격이면 False가 출력되게하세요

#input 90 81 86 80
#Output True

korean, english, math, sieence = map(int, input().split(' '))
print(korean >= 90 and english > 80 and math > 85 and sieence>=80)