from django.shortcuts import render
from django.http import HttpResponse
from django.db import connection
from sympy import content
from userapp.models import User
from board.models import Question
# Create your views here.
def index(request):
    rank_list = User.objects.all().order_by('-score')
    return render(
        request,
        'main/index.html',
        {'rank_list': rank_list}
    )

def index2(request):
    rank_list = User.objects.all().order_by('-score')
    return render(
        request,
        'main/index2.html',
        {'rank_list': rank_list}
    )

def search(request):
    if request.method == 'POST':
        search = request.POST.get('search')
        sel=request.POST.get('sel')
        
        
        print(sel)
        result=Question.objects.filter(subject__contains=search)
        return render(
                request,
                'main/show.html',
                {'data':result}
            )

    
