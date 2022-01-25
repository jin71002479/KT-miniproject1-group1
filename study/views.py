from django.shortcuts import render
from django.http import HttpResponse
# from .models import rank_data
from django.db import connection
from userapp.models import User
# Create your views here.

def studying(request):
    return render(
        request,
        'study/studying.html',
    )

