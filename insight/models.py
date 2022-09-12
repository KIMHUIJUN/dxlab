from django.db import models
from common.models import User
# Create your models here.
class Question(models.Model):

    subject = models.TextField()
    content = models.TextField()
    ex_1 = models.CharField(max_length=100, default="보기 없음")
    ex_2 = models.CharField(max_length=100, default="보기 없음")
    ex_3 = models.CharField(max_length=100, default="보기 없음")
    ex_4 = models.CharField(max_length=100, default="보기 없음")
    answer = models.IntegerField(default=0)
    participants = models.IntegerField(default=0)
    correct_person = models.IntegerField(default=0)

    def __str__(self):
        return self.subject


