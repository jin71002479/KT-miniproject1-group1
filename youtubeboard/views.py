from django.shortcuts import render


def index(request):
    return render(request, 'youtubeboard/index.html')

def index2(request):
    return render(request, 'youtubeboard/index2.html')