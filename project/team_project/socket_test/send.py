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
