from django import forms
from .models import Question, Answer

class QuestionForm(forms.ModelForm):
    # upload = forms.FileField(label='첨부 파일', required=False, 
    #       widget=forms.FileInput(attrs={'class': 'form'}))
    class Meta:
        model = Question
        fields = ['subject', 'content', 'file']
       
        labels = {
            'subject': '제목',
            'content': '내용',
            
        }
        def __init__(self, *args, **kwargs):
            super(PostForm, self).__init__(*args, **kwargs)
            self.fields['file'].required = False
        # exclude = ['file']


class AnswerForm(forms.ModelForm):
    
    class Meta:
        model = Answer
        fields = ['content']
        labels = {
        'content': '답변내용',
        }



# class UploadFileForm(forms.ModelForm):
#     class Meta:
#         model = Question
#         fields = ['file']

