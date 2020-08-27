# 가장큰수
# https://programmers.co.kr/learn/courses/30/lessons/42746


def solution(numbers):
	numbers = list(map(str, numbers))
	# print(numbers)
	for i in range(len(numbers)):
		tmp_val1 = numbers[i]
		tmp_val2 = numbers[i] * 4
		# 6666, 2222, 1010 으로 변형되며 숫자간 크기의 구별이 가능해진다.
		numbers[i] = [ tmp_val1, tmp_val2[:4]]
	numbers.sort(key=lambda x: x[1], reverse=True)
	
	# print(numbers)
	result_list = [num[0] for num in numbers]
	result = int(''.join(result_list))

	return str(result)

#numbers = [3, 30, 34, 5, 9]
numbers = [6, 10, 2]
print(solution(numbers))


# 시간초과
# from itertools import permutations

# def solution(numbers):
#     all_list_num = list(permutations(numbers))
#     #print(all_list_num)
#     max_val = 0
#     temp_d = [ ''.join(list(map(str, [i for i in d])))  for d in all_list_num]
#     #print(temp_d)
# 	while temp_d:
# 		tmp_val = int(temp_d.pop(0))
# 		if max_val < tmp_val:
# 			max_val = tmp_val

#     return int(max_val)

#numbers = [3, 30, 34, 5, 9]
numbers = [6, 10, 2]
print(solution(numbers))

# 시간초과 + 런타임 에러
# def recur(numbers, start, val, max_val):
# 	if len(numbers) == 0:
# 		#print(f"val : {val}")
# 		if max_val[0] < int(val):
# 			max_val[0] = int(val)
# 			# print(f"val : {val}")
# 	else:
# 		for _ in range(len(numbers)):
# 			# print(f"numbers[{i}] : {numbers[i]} ")
# 			tmp_val = numbers.pop(0)
# 			tmp_val2 = val
# 			val += str(tmp_val)
# 			recur(numbers, start, val, max_val)
# 			numbers.append(tmp_val)
# 			val = tmp_val2

# def solution(numbers):
# 	start = 0
# 	val = ''
# 	max_val = [0]
# 	recur(numbers, start, val, max_val)
	
# 	return str(max_val[0])