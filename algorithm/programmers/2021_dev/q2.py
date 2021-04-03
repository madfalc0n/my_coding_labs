def mov(m,q):
    x1,y1 = [q[0]-1,q[1]-1]
    x2,y2 = [q[2]-1,q[3]-1]

    old = m[x1][y1]
    min_val = old
    for i in range(y1+1,y2+1):
        old, m[x1][i] =  m[x1][i], old
        min_val = min(min_val, m[x1][i])

    for i in range(x1+1,x2+1):
        old, m[i][y2] =  m[i][y2], old
        min_val = min(min_val, m[i][y2])

    for i in range(y2-1,y1-1,-1):
        old, m[x2][i] =  m[x2][i], old
        min_val = min(min_val, m[x2][i])

    for i in range(x2-1,x1-1,-1):
        old, m[i][y1] =  m[i][y1], old
        min_val = min(min_val, m[i][y1])

    # print(m)

    return [min_val,m]

def solution(rows, columns, queries):
    # print(queries)
    m = []
    for i in range(rows):
        min_v = i * rows + 1
        max_v = (i+1) * rows 
        m.append(list(range(min_v,max_v+1)))

    print(m)

    min_result = []
    for q in queries:
        min_val, m = mov(m,q)
        min_result.append(min_val)
        # print(m)
        # print()
        # m = chg_array(m,tmp_list,q)

    return min_result

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))

