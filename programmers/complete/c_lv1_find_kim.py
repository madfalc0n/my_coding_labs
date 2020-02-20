# 서울에서 김서방 찾는 문제
# 리스트 내 특정 문자열의 인덱스를 반환해주면 끝나는 문제 index 함수를 사용

def solution(seoul):
    return '김서방은 '+str(seoul.index('Kim'))+'에 있다.' 

seoul = ['Jane', 'Kim']
print(solution(seoul))