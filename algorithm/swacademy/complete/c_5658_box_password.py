"""
보물상자의 비밀번호
https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AWXRUN9KfZ8DFAUo&categoryId=AWXRUN9KfZ8DFAUo&categoryType=CODE
17:48 시작
18:15 종료
x진수에서 10진수로 변환, https://brownbears.tistory.com/467
"""
tc = int(input())
for case in range(1,tc+1):
    n, k = list(map(int, input().split()))
    str_list = input()
    lotate = n // 4
    save_set = set()
    for cnt in range(1,lotate+1):
        # print(cnt)
        # print(str_list)
        tmp_i = 0
        while tmp_i < n:
            save_set.add(str_list[tmp_i:tmp_i+lotate])
            # print(str_list[tmp_i:tmp_i+lotate])
            tmp_i += lotate
        tmp_list = list(str_list)
        tmp_val = [tmp_list.pop(-1)]
        tmp_list = tmp_val + tmp_list
        str_list = ''.join(tmp_list)

    result_val = sorted(save_set, reverse=True)[k-1]
    result_val = int(result_val,16)
    print(f"#{case} {result_val}")