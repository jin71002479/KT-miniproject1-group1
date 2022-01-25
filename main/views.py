from django.shortcuts import render
from django.http import HttpResponse
# from .models import rank_data
from django.db import connection
from userapp.models import User
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