from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from userapp.models import User

# Create your views here.
