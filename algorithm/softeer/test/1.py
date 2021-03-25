import sys

K,P,N = list(map(int,input().split(' ')))

result = K
for i in range(N):
        result *= P
print(result % 1000000007)