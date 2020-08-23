com_list = list(map(int, input().split(' ')))
vuno_list = sorted(list(map(int, input().split(' '))))

# print(com_list)

# print(vuno_list)

i = 0
result = 5
while vuno_list:
	if 	com_list[i] > max(vuno_list):
		result -= 1
		com_list.pop(0)
		vuno_list.pop(0)
	elif com_list[i] <= max(vuno_list):
		j = 0
		while j < len(vuno_list):
			if vuno_list[j] >= com_list[i]:
				com_list.pop(0)
				vuno_list.pop(j)
				break
			j += 1
print(result)