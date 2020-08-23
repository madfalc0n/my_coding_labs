def arrive_recue(arr_list, src, dest, cnt):
	if src == dest:
		arr_list.append(cnt)
		# print(arr_list)
	if src > dest:
		arrive_recue(arr_list, src - 1, dest, cnt + 1)
	else:
		arrive_recue(arr_list, src - 1, dest, cnt + 1)
		arrive_recue(arr_list, src + 1, dest, cnt + 1)
		arrive_recue(arr_list, src * 2, dest, cnt + 1)

ye, dong = list(map(int, input().split(' ')))

# print(ye,dong)

cnt = 0
arr_list = list()
arrive_recue(arr_list, ye, dong, cnt)

print(min(arr_list))