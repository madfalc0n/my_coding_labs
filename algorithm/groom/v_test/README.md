# 신경망 크기

```python
n = int(input())
layers = [ int(value) for value in input().split() ]

answer = 0
i = 0
while i < n - 1:
	answer += (layers[i] * layers[i+1])
	i += 1

print(answer)
```

## 369 게임

```python
def tab_recur(num):
	if num < 10:
		if num % 3 == 0 and num != 0:
			return 1
		else:
			return 0
	return tab_recur(num // 10) + tab_recur(num % 10)
	

user_input = int(input())
i = 1
tap_cnt = 0
while i <= user_input:
		tap_cnt += tab_recur(i)
		i += 1
print(tap_cnt)
```

## 배드민턴 경기

```python
com_list = list(map(int, input().split(' ')))
vuno_list = sorted(list(map(int, input().split(' '))))

# print(com_list)

# print(vuno_list)

i = 0
result = 5
while vuno_list:
	if 	com_list[i] > max(vuno_list):
		result -= 1
		com_list.pop(0)
		vuno_list.pop(0)
	elif com_list[i] <= max(vuno_list):
		j = 0
		while j < len(vuno_list):
			if vuno_list[j] >= com_list[i]:
				com_list.pop(0)
				vuno_list.pop(j)
				break
			j += 1
print(result)
```

## 길찾기(다이아몬드)

```python
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
```



## 숨바꼭질

예하와 동생의 숨바꼭질

동생은 주어진 값에서 가만히 있고 

예나만 움직이는데 위치에 따라 1초후 X-1 X+2 순간이동(2X)가능

```python
def arrive_recue(arr_list, src, dest, cnt):
	if src == dest:
		arr_list.append(cnt)
		# print(arr_list)
	if src > dest:
		arrive_recue(arr_list, src - 1, dest, cnt + 1)
	else:
		arrive_recue(arr_list, src - 1, dest, cnt + 1)
		arrive_recue(arr_list, src + 1, dest, cnt + 1)
		arrive_recue(arr_list, src * 2, dest, cnt + 1)

ye, dong = list(map(int, input().split(' ')))

# print(ye,dong)

cnt = 0
arr_list = list()
arrive_recue(arr_list, ye, dong, cnt)

print(min(arr_list))
```