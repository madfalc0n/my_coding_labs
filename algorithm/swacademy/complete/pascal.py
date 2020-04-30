"""
파스칼 삼격형 으로 구현하기

"""
for i in range(int(input())):
    print(f"#{i+1}")
    for j in range(int(input())):
        print(f"{' '.join(str(11**j))}")



# test_case = int(input())
# test_list = []
#
# for i in range(test_case):
#     temp_input = int(input())
#     test_list.append(temp_input)
#
#
#
# for iburn, num in enumerate(test_list):
#     print(f"#{iburn+1}")
#     test_result = []
#     for num2 in range(num):
#         if num2 == 0:
#             #print("1")
#             test_result.append([1])
#         elif num2 == 1:
#             #print("1 1")
#             test_result.append([1,1])
#         else:
#             temp_list_list = []
#             for num3 in range(num2+1):
#                 #print(f"number2 : {num2}, number3 : {num3}")
#                 if num3 == 0 or num3 == num2:
#                     temp_list_list.append(1)
#                 else:
#                     temp_sum = test_result[num2-1][num3-1]  + test_result[num2-1][num3]
#                     temp_list_list.append(temp_sum)
#                 #print(temp_list_list)
#             test_result.append(temp_list_list)
#
#     #print(test_result)
#
#     for n in test_result:
#         for j in n:
#             print(j, end=' ')
#         print()