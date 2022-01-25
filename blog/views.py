from django.shortcuts import render



def index(request):
    return render(request, 'blog/index.html')

def index2(request):
    return render(request, 'blog/index2.html')
