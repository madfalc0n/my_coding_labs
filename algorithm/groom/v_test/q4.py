num = int(input())
t_len = 2*(num - 1) + 1
matrix = [[0] * (num) for i in range(t_len)]

for i in range(len(matrix)):
	matrix[i] = list(map(int, input().split(' ')))

cnt = 0
for i in range(1, t_len):
	for j in range(len(matrix[i])):
		if i < num:
			if j == 0:
				matrix[i][j] += matrix[i-1][j]
			elif j == len(matrix[i]) - 1:
				matrix[i][j] += matrix[i-1][j-1]
			else:
				matrix[i][j] += max(matrix[i-1][j-1] , matrix[i-1][j])
		elif i >= num:
			matrix[i][j] += max(matrix[i-1][j+1], matrix[i-1][j])	

# for i in matrix:

# 	print(i)

print(matrix[-1][0])