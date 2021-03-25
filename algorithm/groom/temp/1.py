# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean

from datetime import datetime


def check(val, best_time):
	result = best_time
	
	best_min = datetime.strptime(best_time[0],"%H:%M")
	best_max = datetime.strptime(best_time[1],"%H:%M")
	
	val_min = datetime.strptime(val[0],"%H:%M")
	val_max = datetime.strptime(val[1],"%H:%M")
	
	if best_min > val_min:
		result[0] = val[0]
	
	if best_max > val_max:
		result[1] = val[1]
	
	return result

num = int(input())
m = []
best_time = 0
sw = True
for i in range(num):
	input_time = input().split(' ~ ')
	trans_time_1 = int(input_time[0].replace(':',''))
	trans_time_2 = int(input_time[1].replace(':',''))
	sum_time = set(range(trans_time_1,trans_time_2+1))
	if i == 0:
		best_time = sum_time
	else:
		best_time = best_time & sum_time
		if len(best_time) == 0:
			sw = False
			break
			
if sw == True:
	# print(' ~ '.join(best_time))
	min_val = list(str(min(best_time)))
	min_val.insert(2,':')
	m_v_1 = ''.join(min_val)
	max_val = list(str(max(best_time)))
	max_val.insert(2,':')
	m_v_2 = ''.join(max_val)
	result = m_v_1 + ' ~ ' + m_v_2
	print(result)
else:
	print("-1")