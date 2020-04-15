

input_number = input()
print(f"입력받은 넘버: {input_number}")
list_number_len = []
list_number_list = []

for i in input_number:
    list_len = input()
    list_number = list(map(int, input().split()))
    list_number_len.append(list_len)
    list_number_list.append(list_number)

