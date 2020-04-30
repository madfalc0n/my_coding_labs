import time

start = time.perf_counter() 
#perf_counter()는 sleep 함수를 호출하여 대기한 시간을 포함하여 측정
#process_time()은 실제로 연산하는데 걸린 시간만 측정

def do_something():
    print('Sleeping 1 second...')
    time.sleep(1)
    print('Done Sleeping...')

do_something()
do_something()

finish = time.perf_counter()
print(f"Finished in {round(finish-start,2)} second(s)")