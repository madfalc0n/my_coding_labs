"""
의좋은 형제
https://level.goorm.io/exam/58258/%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98-%ED%9E%88%EC%96%B4%EB%A1%9C%EC%A6%88-%EC%85%80%ED%94%84%EB%A0%88%EB%B2%A8%ED%85%8C%EC%8A%A4%ED%8A%B8-9%EC%B0%A8/quiz/1
"""


J, S = list(map(int,input().split(' ')))
N = int(input())

order = 0 # 0: J, 1: S
p_list = [J,S]
for i in range(1,N+1):
	order %=2
	to_f = p_list[order] // 2
	if p_list[order] % 2 != 0:
		to_f += 1
	p_list[order] //= 2
	p_list[(order+1) % 2] += to_f
	# print(p_list,order)
	order += 1
	
print(f"{p_list[0]} {p_list[1]}")