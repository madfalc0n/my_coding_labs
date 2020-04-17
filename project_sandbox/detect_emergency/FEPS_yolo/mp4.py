import cv2
import time
from multiprocessing import Process, Queue
import yolo_pro

def create_frame(q):
    video = cv2.VideoCapture("swoon.mp4")
    i = 0
    while (True):
        hasFrame, frame = video.read()
        #print(f"process...index : {i}")
        if not hasFrame:
            print("process...end")
            break
        else:#프레임 있을경우 영상 처리 해줘야제
            cpy_frame = cv2.resize(frame, (416, 416))
            cv2.imshow('image', cpy_frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            time.sleep(0.03)
            if i%150 == 0: #30프레임당 큐에 넣기
                q.put(frame)
                print(f"index: {i} INPUT FRAMES")
        i += 1
    video.release()
    cv2.destroyAllWindows()

def processing_frame(q):
    while True:
        print(f"q status: {q}")
        frame = q.get()
        start_time = time.time()
        #print(f"OUTPUT FRAMES : {frame.shape}")
        frame = yolo_pro.yolo(frame)
        cpy_frame = cv2.resize(frame,(416,416))
        cv2.imshow('image2', cpy_frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        #print(f"inference time : {round(time.time()-start_time, 4)}")
        if frame is -1:
            break


if __name__ == '__main__':
    print("Main status")
    working_queue = Queue()
    print("Queue waiting")
    p1 = Process(target=create_frame, args=(working_queue,))
    p2 = Process(target=processing_frame, args=(working_queue,))
    p1.start()
    p2.start()
    print("진행중")