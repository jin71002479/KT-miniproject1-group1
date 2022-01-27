from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from userapp.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required #로그인여부
from django.views.generic.detail import SingleObjectMixin
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage
from userapp.models import User


def index(request):
    now_page = request.GET.get('page', 1)
    question_list = Question.objects.order_by('-pub_date')
    p = Paginator(question_list, 10)
    info = p.get_page(now_page)
    # context = {'question_list': question_list}
    start_page = (int(now_page) - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages

    context = {'info': info,
        'page_range' : range(start_page, end_page + 1)
    }
    return render(request, 'board/question_list.html', context)

def index2(request):
    question_list = Question.objects.order_by('-pub_date')
    context = {'question_list': question_list}
    return render(request, 'board/question_list2.html', context)

def detail(request, question_id):
    question = get_object_or_404(Question, id=question_id)
    context = {
        'question': question
    }
    return render(request, 'board/question_detail.html', context)


from .forms import AnswerForm
@login_required (login_url='userapp:login')
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.username = request.user.username
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    
    context = {'question': question, 'form': form}
    
    return render(request, 'board/question_detail.html', context)


from .forms import QuestionForm
# def question_create(request):
#     if request.method == 'POST':
#         form = QuestionForm(request.POST)
#         # if form.is_valid():
#         question = form.save(commit=False)
#         question.pub_date = timezone.now()
#         question.username = request.user.username
#         question.save()
#         return redirect('board:index')
#     else:
#         form = QuestionForm()

#     context = {'form': form}

#     return render(request, 'board/question_form.html', context)

@login_required (login_url='userapp:login')
def upload3(request):
    user = User.objects.get(username = request.user.username)   
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
             
        if form.is_valid():
            uploadFile = form.save(commit=False)
            if uploadFile.file:        
                name = uploadFile.file.name 
                size = uploadFile.file.size                              
            uploadFile.pub_date = timezone.now()
            uploadFile.username = request.user.username
            uploadFile.save()
            user.score = user.score + 10
            user.save()
            return redirect('board:index')
    else:
        form = QuestionForm()
    return render(
        request, 'board/question_form.html', {'form': form})

@login_required (login_url='userapp:login2')
def upload4(request):
    user = User.objects.get(username = request.user.username)   
    if request.method == 'POST':
        form = QuestionForm(request.POST, request.FILES)
             
        if form.is_valid():
            uploadFile = form.save(commit=False)
            if uploadFile.file:        
                name = uploadFile.file.name 
                size = uploadFile.file.size                              
            uploadFile.pub_date = timezone.now()
            uploadFile.username = request.user.username
            uploadFile.save()
            user.score = user.score + 10
            user.save()
            return redirect('board:index2')
    else:
        form = QuestionForm()
    return render(
        request, 'board/question_form.html', {'form': form})

def update(request, question_id):
    question = Question.objects.get(id=question_id)
    if(question.username == request.user.username):
        if request.method == "POST":
            question.subject = request.POST['subject']
            question.content = request.POST['content']
            question.pub_date = timezone.now()
            
            question.save()
            return redirect('board:index')
        else:
            question=Question()
            return render(request, 'board/update.html', {'question':question})
    else :
        return render(request, 'board/warning.html')


def delete(request, question_id):
    question = Question.objects.get(id=question_id)
    if(question.username == request.user.username):
        question.delete()
        return redirect('board:index')
    return render(request, 'board/warning.html')

# def download(request):
#     question = get_object_or_404(Question, id=question_id)
   
#     # file_url = urllib.parse.unquote(url)
#     filepath = str(settings.BASE_DIR) + ('/media/%s' % question.file.name)
#     filename = os.path.basename(filepath)
#     context = {
#         'question': question
#     }
#     with open(filepath, 'rb') as f:
#         response = HttpResponse(f, content_type='application/octet-stream')
#         response['Content-Disposition'] = 'attachment; filename=%s' % filename
#         return render(request, 'board/question_detail.html', context)

    
#     return render(request, 'board/question_detail.html', context)

    # id = request.GET.get('id')
    # question = Question.objects.get(id=id)
    # filepath = str(settings.BASE_DIR) + ('/media/%s' % question.file.name)
    # filename = os.path.basename(filepath)
    # with open(filepath, 'rb') as f:
    #     response = HttpResponse(f, content_type='application/octet-stream')
    #     response['Content-Disposition'] = 'attachment; filename=%s' % filename
    #     return response

from config import settings
import os
def download(request,question_id):   
    
    question = get_object_or_404(Question, pk=question_id)
    if question.file:
        file_url = question.file.url[1:]
        # filepath = str(settings.BASE_DIR) + ('/media/%s' % question.file.name)   
        if os.path.exists(file_url) :
            with open(file_url, 'rb') as f:
                filename = os.path.basename(file_url)
                response = HttpResponse(f, content_type='application/octet-stream')
                response['Content-Disposition'] = 'attachment; filename=%s' % filename
                return response
    else :  
        return render(request, 'board/delete.html')