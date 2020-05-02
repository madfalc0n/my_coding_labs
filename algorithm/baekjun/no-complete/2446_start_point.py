"""
별찍기
예제를 보고 유추해서 별찍기
첫째 줄에 N(1 ≤ N ≤ 100)이 주어진다.
첫째 줄부터 2×N-1번째 줄까지 차례대로 별을 출력한다.

트
"""
star ='*'
space = ' '
N = int(input())
print_N = N-1
for i in range(print_N):
    output = (space * i) + (star * (print_N-i))
    output = output + star + output[::-1]
    print(output)
print((space * print_N) + star)
for i in range(1,N):
    output = (space * (print_N-i)) + (star * (i))
    output = output + star + output[::-1]
    print(output)
