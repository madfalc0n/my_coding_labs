from django.shortcuts import render, redirect
from django.urls import reverse
from .models import Video

# Create your views here.
def index(request):
    return redirect('/static/hello.html')


def test(request):
    return redirect('/static/video.html')

def video_list(request):
    video_list = Video.objects.all()
    return render(request, 'video/video_list.html', {'video_list': video_list})

def video_new(request):
    if request.method == 'POST':
        title = request.POST['title']
        video_key = request.POST['video_key']
        Video.objects.create(title=title, video_key=video_key)
        return redirect(reverse('video_list'))
    elif request.method == 'GET':
        return render(request, 'video/video_new.html')

def video_detail(request, video_id):
    video = Video.objects.get(id=video_id)
    return render(request, 'video/video_detail.html', {'video': video})