n = int(input())
layers = [ int(value) for value in input().split() ]

answer = 0
i = 0
while i < n - 1:
	answer += (layers[i] * layers[i+1])
	i += 1

print(answer)