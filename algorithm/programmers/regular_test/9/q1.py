#성공

def solution(numbers):
    val_list = set()
    for i in range(len(numbers)):
        for j in range(i+1,(len(numbers))):
            val_list.add(numbers[i]+numbers[j])
    return sorted(list(val_list))

numbers = [2,1,3,4,1]
print(solution(numbers))