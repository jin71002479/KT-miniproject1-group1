from django.db import models

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    pub_date = models.DateTimeField()
    username = models.CharField(max_length=200)
    file = models.FileField(null=True, blank=True)
    # file = models.FileField(upload_to='%Y/%m/%d', null=True)

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()
