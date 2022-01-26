from django import forms
from .models import Freewrite, Comment

class FreewriteForm(forms.ModelForm):
    
    class Meta:
        model = Freewrite
        fields = ['free_subject', 'free_content']
       
        labels = {
            'free_subject': '제목',
            'free_content': '내용',
        }


class CommentForm(forms.ModelForm):
    
    class Meta:
        model = Comment
        fields = ['comment_content']
        labels = {
        'comment_content': '댓글내용',
        }


