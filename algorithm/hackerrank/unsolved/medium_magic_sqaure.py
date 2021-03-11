123
456
789


1,2,3
4,5,6
7,8,9
1,4,7 
2,5,8 
3,6,9
1,5,9 
357 


def dfs(visit, b):
    global result

    if len(b) == 9:
        # print(b)
        result.append(b)
    else:
        for i in range(1,10):
            tmp = i
            if tmp not in visit:
                visit.append(tmp)
                b.append(tmp)
                dfs(visit,b)
                b.pop(-1)
                visit.pop(-1)
        

b = []
result = []
visit = []
dfs(visit, b)
print(result)