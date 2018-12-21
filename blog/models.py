from django.db import models
from django.utils import timezone

# Create your models here.


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField('标题', max_length=50)
    text = models.TextField('文章内容')
    created_date = models.DateTimeField('写作时间', default=timezone.now)
    published_date = models.DateTimeField('发布时间')

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def __str__(self):
        return self.title
