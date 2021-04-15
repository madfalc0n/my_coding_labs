import heapq

name = input()
h_list = [name]
for i in range(len(name)):
	tmp_name = list(name)
	tmp_name = tmp_name[0:i] + tmp_name[i+1:]
	best_name = h_list[0]
	if best_name[0] > tmp_name[0]:
		h_list[0] = ''.join(tmp_name)
	elif best_name[0] == tmp_name[0]:
		heapq.heappush(h_list, ''.join(tmp_name))
	if len(h_list) > 2:
		h_list.pop(-1)
	
print(h_list[0])