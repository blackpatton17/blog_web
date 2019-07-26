from django.db import models

# Create your models here.

class Blog(models.Model):
    title = models.CharField(max_length = 64)
    content=models.TextField()

    def __str__(self):
        return "标题：{}，字数，概要".format(self.title,len(self.content),self.content[:18])

class Article(models.Model) :
    title = models.CharField(max_length = 100)
    category = models.CharField(max_length = 50, blank = True)
    date_time = models.DateTimeField(auto_now_add = True)
    content = models.TextField(blank = True, null = True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-date_time']
