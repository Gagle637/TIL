"""
Python dictionary 연습 문제
"""

# 1. 평균을 구하시오.
scores = {
    '수학': 80,
    '국어': 90,
    '음악': 100
}

# 아래에 코드를 작성해 주세요.
print('==== Q1 ====')
total_scroe = 0
for subject_score in scores.values():
    total_scroe = total_scroe + subject_score
    # total_scroe += subject_score   16의 식과 동일함
avg_score = total_scroe / len(scores)
print(avg_score)



# 2. 반 평균을 구하시오. -> 전체 평균
score = {
    'a': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    },
    'b': {
        '수학': 80,
        '국어': 90,
        '음악': 100
    }
}
# 아래에 코드를 작성해 주세요.
print('==== Q2 ====')

# total_scroe_2 = 0
# for subject_score2_a in score['a'].values():
#     total_scroe_2 += subject_score2_a
# for subject_score2_b in score['b'].values():
#     total_scroe_2 += subject_score2_b
# total_L=len(score['a'])+len(score['b'])
# print(total_scroe_2/total_L)

# count = 0
# total_scroe2=0
# for person_scroe in scores.values():
#     for indi_scroe in person_scroe.values():
#         total_scroe2 += indi_scroe
#         count += 1

# avg_score2 = total_scroe / count
# print(avg_score2)
total_score = 0
count = 0

for person_score in score.values():
    for indivisual_score in person_score.values():
        total_score = total_score + indivisual_score
        # total_score += indivisual_score
        count = count + 1
        # count += 1

avg_score = total_score / count
print(avg_score)

# 3. 도시별 최근 3일의 온도입니다.
citys = {
    '서울': [-6, -10, 5],
    '대전': [-3, -5, 2],
    '광주': [0, -2, 10],
    '부산': [2, -2, 9],
}

# 3-1. 도시별 최근 3일의 온도 평균은?

# 아래에 코드를 작성해 주세요.
print('==== Q3-1 ====')
"""
출력 예시)
서울 : 값
대전 : 값
광주 : 값
부산 : 값
"""

for name, temp in citys.items():
    # name = 서울
    # temp = [-6, -10, 5]
    avg_temp = sum(temp) / len(temp)
    print(f'{name} : {avg_temp:.1f}')

# 3-2. 도시 중에 최근 3일 중에 가장 추웠던 곳, 가장 더웠던 곳은?


# 아래에 코드를 작성해 주세요.
print('==== Q3-2 ====')
count = 0
for name,temp in citys.items():
#첫 기준은 name = '서울', temp = [-6,-10,5]
# 단 한번만 실행되는 조건이 필요
    if count == 0:
        hot_temp = max(temp)
        cold_temp = min(temp)
        hot_city = name
        cold_city = name
    else:
    #최저 온도가 cold_temp 보다 낮으면, cold_temp에 값을 넣고,
    #최고 온도가 hot_temp 보다 높으면, hot_temp에 값을 새로 넣는다.
        if min(temp) <cold_temp:
            cold_temp = min(temp)
            cold_city = name
        if max(temp) > hot_temp:
            hot_temp = max(temp)
            hot_city = name
    # count += 1
print(f'최고로 더웠던 지역은 {hot_city}, 최고로 추웠던 지역 {cold_city} ')
    
        







# 3-3. 위에서 서울은 영상 2도였던 적이 있나요?
#서울 온도 리스트에 2가 있나요?

# 아래에 코드를 작성해 주세요.
print('==== Q3-3 ====')
if 2 in citys['서울']:
    print('네 있어요')
else:
    print('없어요')