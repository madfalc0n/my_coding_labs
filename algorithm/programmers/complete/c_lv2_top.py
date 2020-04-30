def solution(heights):
    answer = [0]*len(heights)

    for i in range(len(heights)-1, 0 , -1): # 4부터 , 3 
        for j in range(i-1, -1 , -1 ):
            if heights[i] < heights[j]: # 4와 3의 값을 비교    3, 2 의 값을 비교
                answer[i] = j+1
                break
    return answer[::-1]
heights = [1,5,3,6,7,6,5]

print(solution(heights))