def perm(lst,n):
	ret = []
	if n > len(lst): return ret

	if n==1:
		for i in lst:
			ret.append([i])
	elif n>1:
		for i in range(len(lst)):
			temp = [i for i in lst]
			temp.remove(lst[i])
			for p in perm(temp,n-1):
				ret.append([lst[i]]+p)

	return ret

print(perm([6,10,2],3))

# def solution(numbers):
#     answers = ''
#     if len(numbers) ==1:
#         return numbers.pop(0)
#     for i in numbers:
#
#
#
#     return answers
#
# #numbers = 	[6,10,2]
# numbers = [3, 30, 34, 5, 9]
#
# print(solution(numbers))



# # 시간초과
# from itertools import permutations
#
# def solution(numbers):
#     all_list_num = list(permutations(numbers,len(numbers)))
#     max_val = 0
#     temp_d = [ ''.join(list(map(str, [i for i in d])))  for d in all_list_num]
#     temp_d.sort()
#     #print(temp_d[-1])
#     # for d in all_list_num:
#     #     temp_alpha = ''
#     #     str_d = ''.join(list(map(str, [i for i in d])))
#     #     #print(str_d)
#     #     if max_val < int(str_d):
#     #         max_val = int(str_d)
#
#     return temp_d[-1]
#
#
# numbers = 	[6,10,2]
#
# print(solution(numbers))