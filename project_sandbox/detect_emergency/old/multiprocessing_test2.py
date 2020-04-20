from multiprocessing import Pool
import time

#perf_counter()는 sleep 함수를 호출하여 대기한 시간을 포함하여 측정
#process_time()은 실제로 연산하는데 걸린 시간만 측정

def do_something(name):
    global global_val
    for i in range(1,100000):
        print(f"{name} : {i}")
        if name == 'p3':
            global_val *= -1
        print(f"글로벌 변수 상태 : {global_val}")


global_val = 1
list1 = ["p1","p2","p3"]
if __name__ == "__main__":
    start_time = time.time()
    with Pool(processes=3) as pool:
        pool.map(do_something,list1)
        pool.close()
        pool.join()

    end_time = time.time()
    print(f"Finished in {round(end_time-start_time,2)} second(s)")

# import multiprocessing
# import time
#
# start_time = time.time()
# #perf_counter()는 sleep 함수를 호출하여 대기한 시간을 포함하여 측정
# #process_time()은 실제로 연산하는데 걸린 시간만 측정
#
# def do_something(name):
#     for i in range(1,500001):
#         print(f"{name} : {i}")
#
#
# list1 = ["p1","p2","p3","p4"]
# if __name__ == "__main__":
#
#     pool = multiprocessing.Pool(processes=3)
#     pool.map(do_something,list1)
#     pool.close()
#     pool.join()
#
# end_time = time.time()
# print(f"Finished in {round(end_time-start_time,2)} second(s)")


# import time
#
# start_time = time.time()
# #perf_counter()는 sleep 함수를 호출하여 대기한 시간을 포함하여 측정
# #process_time()은 실제로 연산하는데 걸린 시간만 측정
#
# def do_something(name):
#     for i in range(1,500001):
#         print(f"{name} : {i}")
#
#
# list1 = ["p1","p2","p3","p4"]
# for num in list1:
#     do_something(num)
#
# end_time = time.time()
# print(f"Finished in {round(end_time-start_time,2)} second(s)")