"""
카카오 코딩테스트,
캐시
캐시 hit 일경우 1초 걸리고 miss 일 경우 5초
캐시에 도시가 있는경우 1초, 없는경우 5초
LRU 알고리즘, 가장 최근에 사용된 적없는 캐시 메모리부터 대체 , 해당 데이터의 인덱스를 마지막으로 위치한다
"""
def change_cache_location(cache_list,cache_index):
    #제일 끝에 넣는다.
    tmp_que = cache_list.pop(cache_index)
    cache_list.append(tmp_que)
    
def solution(cacheSize, cities):
    if cacheSize == 0:
        return len(cities) * 5
    cnt = 0
    cache_list = [cities.pop(0).lower()]
    cnt += 5
    #print(cache_list)
    while cities:
        print(cache_list)
        queue = cities.pop(0).lower()
        #print(queue)
        if queue in cache_list: #캐시에 있는경우
            cnt += 1
            cache_index = cache_list.index(queue)
            change_cache_location(cache_list,cache_index)
        else: #캐시에 없는 경우
            cnt += 5
            if len(cache_list) == cacheSize: #캐시가 꽉찬경우
                cache_list.pop(0)
                cache_list.append(queue)
            else:
                cache_list.append(queue)
        print(cache_list)

    return cnt

cacheSize = 3
cities = ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]
print(solution(cacheSize,cities))
