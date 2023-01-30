from django.shortcuts import render, HttpResponse


# Create your views here.


def index(request):
    return render("欢迎使用")


def news(request):
    return render(request, 'news.html')


def depart_list(request):
    return render(request, 'depart_list.html')
