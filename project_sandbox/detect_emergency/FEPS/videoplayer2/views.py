from django.shortcuts import render, redirect
from django.http import HttpResponse, StreamingHttpResponse
import cv2
import time
from django.views.decorators import gzip
#import module_yolo as yolo


def test(request):
    return render(request, 'video2/hello.html' , {'msg' : 'videoview'})


class VideoCamera(object):
    def __init__(self):
        #self.video = cv2.VideoCapture("http://118.47.72.177:8080/video")
        #self.video = cv2.VideoCapture(0)
        self.video = cv2.VideoCapture("static/videos/godzilla.mp4")
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,image = self.video.read()
        image_size = (256, 144)
        image = cv2.resize(image, image_size)
        #print(ret)
        #image = yolo.yolo(image)
        ret,jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()

class VideoCamera2(object):
    def __init__(self):
        #self.video = cv2.VideoCapture("http://118.47.72.177:8080/video")
        #self.video = cv2.VideoCapture(0)
        self.video = cv2.VideoCapture("static/videos/animal.mp4")
    def __del__(self):
        self.video.release()
    def get_frame(self):
        ret,image = self.video.read()
        #print(ret)
        #image = yolo.yolo(image)
        ret,jpeg = cv2.imencode('.jpg',image)
        return jpeg.tobytes()


def gen(camera):
    while True:
        frame = camera.get_frame()
        #time.sleep(0.003)
        yield(b'--frame\r\n'
        b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')



@gzip.gzip_page
def index(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera()),content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")

@gzip.gzip_page
def index2(request):
    try:
        return StreamingHttpResponse(gen(VideoCamera2()),content_type="multipart/x-mixed-replace;boundary=frame")
    except HttpResponseServerError as e:
        print("aborted")
