import time
from multiprocessing import Process, Queue
import cv2


def create_to_something(datas,que):
    print('Creating data and putting it on the queue')
    for data in datas:
        que.put(data) #데이터의 인자를 하나씩 넣어준다

def send_to_output(que):
    while True:
        data = que.get() #que에 잇는 데이터의 인자를 하나씩 받아온다
        print('data found to be processed: {}'.format(data))
        processed = data * 2
        print(processed)
        if data is -1:
            break




if __name__ == "__main__":
    work = Queue()
    datas = [1,2,3,4,5]
    process_one = Process(target=create_to_something, args=(datas,work) )
    process_two = Process(target=send_to_output, args=(work,))
    process_one.start()
    process_two.start()
    work.close()
    work.join_thread()

    process_one.join()
    process_two.join()