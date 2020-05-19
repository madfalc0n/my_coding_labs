"""
1983 조교의 성적 매기기
평점은 10개있다.
A+ 
A0 
A-
B+ 
B0 
B-
C+ 
C0 
C-
D0 
중간 35% 기말 45% 과제 20%
1. N은 항상 10의 배수이며, 10이상 100이하의 정수이다. (10 ≤ N ≤ 100)
2. K는 1 이상 N 이하의 정수이다. (1 ≤ K ≤ N)
3. K 번째 학생의 총점과 다른 학생의 총점이 동일한 경우는 입력으로 주어지지 않는다.

87 59 88


"""
grade = ['0','A+','A0' ,'A-','B+' ,'B0' ,'B-','C+' ,'C0' ,'C-','D0' ]
for index in range(1,int(input())+1):
    N, k = map(int,input().split(' '))
    cal_n = N // 10
    matrix_dict = {}
    for i in range(N):
        tmp_point_list = list(map(int, input().split(' ')))
        tmp_point = int(tmp_point_list[0]*0.35) + int(tmp_point_list[1]*0.45) + int(tmp_point_list[2]*0.20)
        matrix_dict[i+1] = tmp_point
    sort_matrix_dict = sorted(matrix_dict.items(), key= lambda x: x[1], reverse=True)
    print(sort_matrix_dict)
    order = sort_matrix_dict.index((k,matrix_dict[k]))+1
    order = (order // cal_n) + (order % cal_n)
    print(f"#{index} {grade[order]}")
    