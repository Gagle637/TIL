#2 번쨰 오답 

# number = input('a=?')
# a=int(number)
# Output=a + a*11 + a*111 + a*1111
# print(f' {number}, {Output}')

# 3번쨰 시도
# number = input('')
# a=int(number)
# if 0<a and 10>a:
# 	Output=a + a*11 + a*111 + a*1111
# 	print(f' {number}, {Output}')

# # 4번쨰 시도
# number = input('')
# a=int(number)
# if 0<a and 10>a:
# 	Output=a + a*11 + a*111 + a*1111
# 	print(Output)

# 성공 ps. 아웃풋만 나올것

# N= int(input())
# for i in range(1,N+1):
# 	if i/3:
# 		print(i, end=' ')
# 	elif i%3=0 and i%11==0:
# 		print('--', end=' ')
# 	else:
# 		print('-', end=' ')


start = int(input())
trieagle = int(input())

for i in range(1,trieagle):
    print(f'{i:>trieagle}')
	

	