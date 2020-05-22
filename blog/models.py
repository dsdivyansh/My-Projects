from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
# Create your models here.

class Post(models.Model):
    STATUS_CHOICES=(('draft','Draft'),('published','Published'))
    title=models.CharField(max_length=260)
    slug=models.SlugField(max_length=264,unique_for_date='publish')
    author=models.ForeignKey(User,related_name='blog_posts',on_delete=models.PROTECT)
    body=models.TextField()
    publish=models.DateTimeField(default=timezone.now)
    created=models.DateTimeField(auto_now_add=True)
    updated=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=20,choices=STATUS_CHOICES,default='draft')

    class Meta:
        ordering=('-publish',)
    def __str__(self):
        return self.title

# class Comment(models.Model):
#     post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
#     author = models.CharField(max_length=200)
#     text = models.TextField()
#     created_date = models.DateTimeField(default=timezone.now)
#     approved_comment = models.BooleanField(default=False)
#
#
#     class Meta:
#         ordering = ['created_date']
#
#     def __str__(self):
#         return 'Comment {} by {}'.format(self.body,self.name)

class Comment(models.Model):
    post = models.ForeignKey('blog.Post', on_delete=models.CASCADE, related_name='comments')
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def __str__(self):
        return self.text
