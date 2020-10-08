def solution(n):
    
    val_list = []

    while 1:
        if n < 3:
            val_list.insert(0,n)
            break
        val_2 = n % 3
        n = n // 3
        val_list.insert(0, val_2)

    # print(val_list)
    result = 0
    for i in range(len(val_list)):
        result += (3**i) *  val_list[i]
    return result
        


n = 45
print(solution(n))