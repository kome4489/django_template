from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def index(request):
#     return HttpResponse('hello aaaa  world')

def index(request):
    string = 'aaa'
    results = ['aaa', 'bbb', 'ccc']
    return render(request, 'index.html', { 'string': string, 'results': results })
