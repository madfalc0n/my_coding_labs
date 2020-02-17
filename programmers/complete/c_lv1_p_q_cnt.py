def solution(s):
    answer = True
    s = s.lower()
    print(s)
    if s.count('p') != s.count('y'):
        return False

    return True


s = "pPoooyY"

print(solution(s))