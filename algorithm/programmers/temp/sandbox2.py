from itertools import permutations

def solution(numbers):
    all_list_num = list(permutations(numbers))
    print(all_list_num)
    max_val = 0
    temp_d = [ ''.join(list(map(str, [i for i in d])))  for d in all_list_num]
    print(temp_d)
    temp_d.sort()


    return temp_d[-1]

numbers = [6, 10, 2]

print(solution(numbers))