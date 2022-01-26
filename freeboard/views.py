from django.shortcuts import render
from django.http import HttpResponse
from .models import Freewrite
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from userapp.models import User

def index(request):
    question_list = Freewrite.objects.order_by('-free_pub_date')
    context = {'question_list': question_list}
    return render(request, 'board/question_list.html', context)