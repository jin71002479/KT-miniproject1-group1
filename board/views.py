from django.shortcuts import render
from django.http import HttpResponse
from .models import Question
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from userapp.models import User
from django.core.paginator import Paginator


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
def answer_create(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    
    if request.method == "POST":
        form = AnswerForm(request.POST)
        if form.is_valid():
            answer = form.save(commit=False)
            answer.create_date = timezone.now()
            answer.question = question
            answer.save()
            return redirect('board:detail', question_id=question.id)
    else:
        form = AnswerForm()
    
    context = {'question': question, 'form': form}
    
    return render(request, 'board/question_detail.html', context)


from .forms import QuestionForm
def question_create(request):
    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            question = form.save(commit=False)
            question.pub_date = timezone.now()
            question.username = request.user.username
            question.save()
            return redirect('board:index')
    else:
        form = QuestionForm()

    context = {'form': form}

    return render(request, 'board/question_form.html', context)

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