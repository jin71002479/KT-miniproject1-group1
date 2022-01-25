from django.shortcuts import render
from django.contrib.auth.decorators import login_required #로그인여부
from userapp.models import User

@login_required (login_url='userapp:login')

def main(request): ## 점수 저장
    if request.method == "POST":
        score = request.POST["score"]
        user_score=User.objects.get(username= request.user.username)
        user_score.score=score
        user_score.save()
    return render(request,'Quiz/index.html')