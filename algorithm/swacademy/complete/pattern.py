"""
패턴에서 반복되는 마디의 길이를 출력
각 문자열의 길이는 30, 마디의 최대 길이는 10
반례가있다. 'KOREAKOREAKOREAKOREAKOREAKOREA' 을 입력 할 경우 'KOREA' 도 되고 'KOREAKOREA'도 되기 때문이다.
문제 개선이 필요함
"""

test_case = int(input())
test_list = []
test_result = []
for i in range(test_case):
    temp_input = input()
    test_list.append(temp_input)

for sen in test_list:
    max = 10
    temp_len = len(sen)
    #print(sen)
    for i in range(1, temp_len//2+1):
        if i > 10:
            break
        #print(sen[:i] , sen[i:i*2])
        if sen[:i] == sen[i:i*2]:
            if max > i:
                max = i
    test_result.append(max)

#print(max)

for i,j in enumerate(test_result):
    print(f"#{i+1} {j}")