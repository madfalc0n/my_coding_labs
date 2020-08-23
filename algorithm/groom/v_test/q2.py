def tab_recur(num):
	if num < 10:
		if num % 3 == 0 and num != 0:
			return 1
		else:
			return 0
	return tab_recur(num // 10) + tab_recur(num % 10)
	

user_input = int(input())
i = 1
tap_cnt = 0
while i <= user_input:
		tap_cnt += tab_recur(i)
		i += 1
print(tap_cnt)