for index in range(1,int(input())+1):
    case_number = int(input())
    sum_salary = 0
    for i in range(case_number):
        p,x = map(float,  input().split(' '))
        sum_salary += p*x
        #print(p,x)
    print(f"#{index} {sum_salary:6f}")