def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        bin_arr = bin(arr1[i] | arr2[i])[2:]
        bin_arr = bin_arr.replace('1','#').replace('0',' ')
        len_bin = len(bin_arr)
        if len_bin != n:
            bin_arr = ' '*(n-len_bin) + bin_arr
        #print(bin_arr)
        answer.append(bin_arr)
        
    return answer

n = 5
arr1 = [9, 20, 28, 18, 11]
arr2 = [30, 1, 21, 17, 28]
print(solution(n,arr1,arr2))