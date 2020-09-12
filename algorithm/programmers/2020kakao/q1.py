
#대 - >소문자 변경
def step1(new_id):
    new_id = new_id.lower()
    return new_id

#소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.) 제거
def step2(new_id):
    tmp_list = []
    for i in range(len(new_id)):
        tmp = new_id[i]
        if ('a' <= tmp <= 'z') or ('0' <= tmp <= '9') or tmp == '-' or tmp == '_' or tmp == '.':
            tmp_list += str(new_id[i])
    tmp_list = ''.join(tmp_list)
    return tmp_list

#마침표 2번 이상 연속되는거 하나로 치환
def step3(new_id):
    tmp_list = ''
    cnt = 0
    for i in range(len(new_id)):
        if new_id[i] == '.' and cnt == 0:
            tmp_list += new_id[i]
            cnt += 1
        if new_id[i] != '.':
            tmp_list += new_id[i]
            cnt = 0

    return tmp_list

#마침표가 처음이나 끝에있으면 제거
def step4(new_id):
    if len(new_id) == 0:
        return new_id

    if new_id[0] == '.':
        new_id = new_id[1:]

    if len(new_id) == 0:
        return new_id

    if new_id[-1] == '.' :
        new_id = new_id[:-1]
    return new_id

#빈문자열이면 a를 대입
def step5(new_id):
    if len(new_id) == 0:
        new_id += 'a'
    return new_id

#길이가 16 이상이면 15개 문자를 제외한 나머지 문자 제거
def step6(new_id):
    if len(new_id) >= 16:
        new_id = new_id[:15]
    if new_id[-1] == '.':
        new_id = new_id[:-1]
    return new_id

# 2자 이하라면 길이가 3될 때 까지 반복해서 생성
def step7(new_id):
    if len(new_id) <= 2:
        tmp = new_id[-1]
        while True:
            new_id += tmp
            if len(new_id) == 3:
                break
    return new_id

def solution(new_id):
    new_id = step1(new_id)
    new_id = step2(new_id)
    new_id = step3(new_id)
    new_id = step4(new_id)
    new_id = step5(new_id)
    new_id = step6(new_id)
    new_id = step7(new_id)

    return new_id


new_id = ""
print(solution(new_id))
# new_id = "...!@BaT#*..y.abcdefghijklm"
# print(solution(new_id))
# new_id = "z-+.^."
# print(solution(new_id))
# new_id = "=.="
# print(solution(new_id))
# new_id = "123_.def"
# print(solution(new_id))
# new_id = "abcdefghijklmn.p"
# print(solution(new_id))