from django.shortcuts import render
from django.http import HttpResponse
from .models import Freewrite
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from userapp.models import User

def index(request):
    freewrite_list = Freewrite.objects.order_by('-free_pub_date')
    context = {'freewrite_list': freewrite_list}
    return render(request, 'freeboard/freewrite_list.html', context)