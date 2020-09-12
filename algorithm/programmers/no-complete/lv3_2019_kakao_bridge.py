"""
징검다리 건너기
https://programmers.co.kr/learn/courses/30/lessons/64062
"""
def isPossible(stones, k, mid):
    disappearedStones = 0
    
    for s in stones:
        if s - mid <= 0:
            disappearedStones += 1
            if disappearedStones == k:
                return False
        else:
            disappearedStones = 0
            
    return True
 
    
def solution(stones, k):
    answer = 0
    
    left = 0
    right = 200000000
    
    while left <= right:
        mid = (left + right) // 2
        
        if isPossible(stones, k, mid):
            answer = mid
            left = mid + 1
        else:
            right = mid - 1
    
    return answer + 1




stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
print(solution(stones,k))