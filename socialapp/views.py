from django.shortcuts import HttpResponse

def index(reques):
    return HttpResponse('hello world')