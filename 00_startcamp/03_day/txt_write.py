# 1. 변수에 만들고 싶은 파일을 open() 해야 한다.
# open() 할때 r : 일기 / w : 쓰기(+덮어쓰기) / a : 추가
#f = open('만들 파일 명', '행동')
f = open('ssafy.txt', 'w')
# 1~10까지 입력 
for i in range(10):
    f.write(f'This is line {i+1}.\n')
f.close()
#  \n은 Enter의 역할을 한다.

# with 구문(context manager)
with open('with_ssafy.txt','w') as f:
    for i in range(10):
        f.write(f'This is line {i+1}.\n')

#writslines() : list를 넣어주면, 요소 하나당 한 줄씩 작성한다.
with open('ssafy.txt','w') as f:
    f.writelines(['0\n','1\n','2\n','3\n'])

# 이스케이프 문자
# \n : 개행문자(다음줄이동)
# \t : Tab 문자
# \\ : \(백슬래쉬)문자 사용
# \' : 따음표 사용
# \" : 쌍따음표 사용됨
# 첫번째 \는 출력되지않는다.ㅅ