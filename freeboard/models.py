from django.db import models

class Freewrite(models.Model):
    free_subject = models.CharField(max_length=200)
    free_content = models.TextField()
    free_pub_date = models.DateTimeField()

class Comment(models.Model):
    freewrite = models.ForeignKey(Freewrite, on_delete=models.CASCADE)
    comment_content = models.TextField()
    comment_create_date = models.DateTimeField()