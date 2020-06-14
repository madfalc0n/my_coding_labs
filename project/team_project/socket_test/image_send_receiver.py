
# 송시자(클라이언트)
import socket 
import numpy as np
import cv2
import pickle
import struct
import io
import time
import zlib


def recvall(sock, count):
    buf = b''
    while count:
        newbuf = sock.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


HOST = '13.124.193.28'
PORT = 8893

#img = cv2.imread(cur_dir+'\test.PNG')
img = cv2.imread('c:/Users/user/Desktop/kmh/my_coding_labs/project/team_project/socket_test/test.PNG')
print(img.shape)
encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
img = cv2.imencode('.jpg', img, encode_param)
data = pickle.dumps(img, protocol=3)
#data = pickle.dumps(img, 0)
size = len(data)
print(size)

client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM) 
connection = client_socket.makefile('wb')
client_socket.connect((HOST, PORT)) 


while True: 
    client_socket.sendall(struct.pack(">L", size) + data)
    break
    # message = '1'
    # client_socket.send(message.encode()) 
  
    # length = recvall(client_socket,16)
    # stringData = recvall(client_socket, int(length))
    # data = np.frombuffer(stringData, dtype='uint8') 

    # decimg=cv2.imdecode(data,1)
    # #cv2.imshow('Image',decimg)
    
    # key = cv2.waitKey(1)
    # if key == 27:
    #     break

print('close socket')
client_socket.close() 



# 수신자(서버)
import socket
import cv2
import matplotlib.pyplot as plt
import struct ## new
import zlib
import sys
import pickle
import numpy as np
TCP_IP = 'IPaddress'
TCP_PORT = servicePort

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print('Socket created')

s.bind((TCP_IP,TCP_PORT))
print('Socket bind complete')
s.listen(10)
print('Socket now listening')

conn,addr=s.accept()

data = b""
payload_size = struct.calcsize(">L")
print("payload_size: {}".format(payload_size))
while True:
    while len(data) < payload_size:
        print("Recv: {}".format(len(data)))
        data += conn.recv(4096)

    print("Done Recv: {}".format(len(data)))
    packed_msg_size = data[:payload_size]
    data = data[payload_size:]
    msg_size = struct.unpack(">L", packed_msg_size)[0]
    print("msg_size: {}".format(msg_size))
    while len(data) < msg_size:
        data += conn.recv(4096)
    frame_data = data[:msg_size]
    data = data[msg_size:]
    
    s.close()
    #pick_data=pickle.loads(frame_data, fix_imports=True, encoding="bytes")
    pick_data=pickle.loads(frame_data)
    #print(frame)
    #print(np.load(image))
    print(pick_data)
    print(len(pick_data))
    image = cv2.imdecode(pick_data[1], cv2.IMREAD_COLOR)
    #image = cv2.imdecode(pick_data, -1)
    plt.imshow('ImageWindow',image)
    
    break