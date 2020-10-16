"""
시험감독
https://www.acmicpc.net/problem/13458
01:40 시작
2:05 종료
"""
n = int(input())
users = list(map(int,input().split()))
cap,sub_cap = list(map(int,input().split()))

users_dict = dict()
for user in users:
    users_dict[user] = users_dict.get(user,0) + 1

result = 0
for user in users_dict.keys():
    total = user - cap
    need_cap = 1
    if total >= 0: #총 감독관 1명으로 모자랄 때
        if total % sub_cap != 0: 
            need_cap += ((total // sub_cap) + 1)
        else:
            need_cap += (total // sub_cap)
    result += users_dict[user] * need_cap
print(result)