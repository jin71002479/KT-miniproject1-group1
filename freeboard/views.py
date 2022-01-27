from django.shortcuts import render
from django.http import HttpResponse
from .models import Freewrite,Comment
from django.shortcuts import get_object_or_404
from django.utils import timezone
from django.shortcuts import redirect
from userapp.models import User
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required #로그인여부

def index(request):
    now_page = request.GET.get('page', 1)
    freewrite_list = Freewrite.objects.order_by('-free_pub_date')
    p = Paginator(freewrite_list, 10)
    freeinfo = p.get_page(now_page)
    start_page = (int(now_page) - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages

    context = {'freeinfo': freeinfo,
        'page_range' : range(start_page, end_page + 1)
    }
    return render(request, 'freeboard/freewrite_list.html', context)

def index2(request):
    now_page = request.GET.get('page', 1)
    freewrite_list = Freewrite.objects.order_by('-free_pub_date')
    p = Paginator(freewrite_list, 10)
    freeinfo = p.get_page(now_page)
    start_page = (int(now_page) - 1) // 10 * 10 + 1
    end_page = start_page + 9
    if end_page > p.num_pages:
        end_page = p.num_pages

    context = {'freeinfo': freeinfo,
        'page_range' : range(start_page, end_page + 1)
    }
    return render(request, 'freeboard/freewrite_list2.html', context)


def detail(request, freewrite_id):
    freewrite = get_object_or_404(Freewrite, id=freewrite_id)
    context = {
        'freewrite': freewrite
    }
    return render(request, 'freeboard/freewrite_detail.html', context)


from .forms import CommentForm
@login_required (login_url='userapp:login')
def comment_create(request, freewrite_id):
    freewrite = get_object_or_404(Freewrite, pk=freewrite_id)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comment_create_date = timezone.now()
            comment.freewrite = freewrite
            comment.username = request.user.username
            comment.save()
            return redirect('freeboard:detail', freewrite_id=freewrite.id)
    else:
        form = CommentForm()
    
    context = {'freewrite': freewrite, 'form': form}
    
    return render(request, 'freeboard/freewrite_detail.html', context)


from .forms import FreewriteForm
from userapp.models import User
@login_required (login_url='userapp:login')
def freewrite_create(request):
    user = User.objects.get(username = request.user.username)
    if request.method == 'POST':
        form = FreewriteForm(request.POST)
        if form.is_valid():
            freewrite = form.save(commit=False)
            freewrite.free_pub_date = timezone.now()
            freewrite.username = request.user.username
            freewrite.save()
            user.score = user.score + 5
            user.save()
            return redirect('freeboard:index')
    else:
        form = FreewriteForm()

    context = {'form': form}

    return render(request, 'freeboard/freewrite_form.html', context)
@login_required (login_url='userapp:login')
def freewrite_create2(request):
    user = User.objects.get(username = request.user.username)
    if request.method == 'POST':
        form = FreewriteForm(request.POST)
        if form.is_valid():
            freewrite = form.save(commit=False)
            freewrite.free_pub_date = timezone.now()
            freewrite.username = request.user.username
            freewrite.save()
            user.score = user.score + 5
            user.save()
            return redirect('freeboard:index2')
    else:
        form = FreewriteForm()

    context = {'form': form}

    return render(request, 'freeboard/freewrite_form2.html', context)


def update(request, freewrite_id):
    freewrite = Freewrite.objects.get(id=freewrite_id)
    if(freewrite.username == request.user.username):
        if request.method == "POST":
            freewrite.free_subject = request.POST['subject']
            freewrite.free_content = request.POST['content']
            freewrite.free_pub_date = timezone.now()
            
            freewrite.save()
            return redirect('freeboard:index')
        else:
            freewrite=Freewrite()
            return render(request, 'freeboard/update.html', {'freewrite':freewrite})
    else :
        return render(request, 'freeboard/warning.html')


def delete(request, freewrite_id):
    freewrite = Freewrite.objects.get(id=freewrite_id)
    if(freewrite.username == request.user.username):
        freewrite.delete()
        return redirect('freeboard:index')
    return render(request, 'freeboard/warning.html')


def comment_delete(request,comment_id):
    comment = Comment.objects.get(id=comment_id)
    if(comment.username == request.user.username):
        comment.delete()
        return redirect('freeboard:index')
    return render(request, 'freeboard/warning.html')