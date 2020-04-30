import math

def solution(progresses, speeds):
    # 걸리는 시간 계산
    send_time = []
    for i, j in zip(progresses,speeds):
        #print(i , j )
        ##print(100-i/j)
        send_time.append(math.ceil((100-i)/j))
    #print(send_time)
    
    min_time = 0
    work_time ={}
    for i in send_time:
        if min_time < i:
            min_time = i
        work_time[min_time] = work_time.get(min_time,0) +1
    #print(work_time)

    result = [ i for i in work_time.values()  ]
    #print(result)
    
    return result



progresses = [93,30,55]
speeds = [1,30,5]

#print(solution(progresses, speeds))