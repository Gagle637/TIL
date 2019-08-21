from django.db import models

# Create your models here.
class Article(models.Model): #models.Model의 상속
#id는 프라이머리 키는 기복적으로 처음 테이블 생성시 자동으로 만들어진다.
    # id = models.AutoField(primary_key=True) #클래시 변수(DB의 필드)
    title = models.CharField(max_length=10) 
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.pk}번글 - {self.title} : {self.content}'