#코딩 도장 Unit10 ~  

#range와 list
print(list(range(-4,10,2)))
#range(시작,끝,증가폭) list는 리스트를 만드는 함수

print(list(range(10,0,-1)))
#감소 역시 가능합니다.

#튜플 list과 비슷하지만 안에 저장된 요소를 변경, 추가, 삭제를 할 수 없습니다.
#list
practice_list = ['a', 1, 2, 3]
practice_tuple = (38, 21, 53, 'a', True)  #괄호는 생략이 가능합니다.
print(practice_list, practice_tuple, sep='\n')
#tuple(), list()를 이용해 서로 변경이 가능합니다.

#시퀸스 자료형은 리스트(list), 튜플(tuple), 레인지(range)
#range를 제외하고 시퀸스 객체는 +연산자를 이용해 연결할 수 있습니다.
print(practice_list+practice_list)
print(practice_tuple+practice_tuple)
print('Hello'+'world!') 
#문자열 역시 연결이 가능합니다.

# range를 제외하고 *연산자를 이용하여 반복이 가능합니다.
print(practice_list*3)

#len()을 이용해 튜플의 요소를 구할 수 있습니다.
print(len(practice_list))

#인덱스 사용하기 시퀸스객체[인덱스] 을 이용하면 해당요소에 접근이 가능합니다. 
#시퀸스 객체의 인덱스는 항상 0부터 시작합니다.
print(practice_list[0])
print(practice_list.__getitem__(0))
print(practice_list[-1])
#뒤에서 첫번재란 뜻으로 - 사용역시 가능합니다.

practice_list[0] = 'b'
print(practice_list[0])
#다음과 같이 수정도 가능합니다. 다만 practice_list[5] = False 와 같이 범위를 벗어난 인덱스는 지정할수 없습니다.
#튜플과 레인지, 문자열의 경우는 수정이 불가능합니다. 이들은 읽기전용 스퀸스 자료형입니다.

print(practice_list)
del practice_list[1]
print(practice_list)


#슬라이스 사용하기  시퀸스객체[시작인덱스:끝인덱스]
practice_list = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print(practice_list[0:4])
#마지막은 가져오려 하지않습니다. 즉 위의 리스트를 모두 출력하기 위해선 print(practice_list[0:10])을 사용하여야 합니다.

#시퀸스객체[시작인덱스:끝인덱스:인덱스증가폭] range와 문자열, 튜플, list 모두 사용이 가능합니다.
print(practice_list[2:8:3])
print(practice_list[:7]) #6까지 가져옴
print(practice_list[7:]) #7부터 마지막요소까지 가져옵니다.
print(practice_list[:]) #전체를 가져옴
print(practice_list[::2]) #0부터 2씩 증가하며 가져옴

#슬라이스 객체 = slice(시작,끝,인덱스증가폭) 시퀸스를 잘라낼수 있습니다.
print(range(10)[slice(4,7,2)])
print(range(10).__getitem__(slice(4,7,2)))

#s = slice(4,7)
#a[s] 의 방법으로 a에게 s에 저장된만큼슬라이스 하는것 역시 가능합니다.



