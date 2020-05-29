from django.shortcuts import render
from django.http import HttpResponse
from app_1.models import User

# Create your views here.
def index(request):
    return HttpResponse("Helllo django")


def listuser(request):
    q = request.GET.get('q','')
    if q == '':
        data = User.objects.all()
    else:
        data = User.objects.all().filter(name__contains=q)
    return render(request, 'test.html', {'data':data})


def tester(request):
    return render(request, 'test2.html', {'data':1})