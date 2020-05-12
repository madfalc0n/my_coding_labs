def solution(board, moves):
    stack = []
    answer = 0
    while moves:#0~N 까지
        tmp_pop = moves.pop(0) - 1
        for i in range(len(board)):
            if board[i][tmp_pop] != 0 : #0이 아닐때 인형뽑기ㄱㄱ
                #print(board[i][tmp_pop])
                stack.append(board[i][tmp_pop])
                board[i][tmp_pop] = 0
                break
        if len(stack) >= 2:
            if stack[-1] == stack[-2]:
                stack.pop()
                stack.pop()
                answer += 2

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]	
print(solution(board,moves))