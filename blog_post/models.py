from django.db import models
LIKING_STATUS = (('like', 'like'), ('dislike', 'dislike'), ('no response', 'no response'))

class Post(models.Model):
    created_by=models.CharField(max_length=80)
    title = models.CharField(max_length=80)
    body = models.TextField()
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return str(self.title)

LIKING_STATUS = (('like', 'like'), ('dislike', 'dislike'), ('no response', 'no response'))
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    comment_by=models.CharField(max_length=80,blank=True,null=True)
    body = models.TextField()
    like_status = models.CharField(max_length=100, choices=LIKING_STATUS, default='no response')
    pub_date = models.DateTimeField('date published', auto_now_add=True)
    def __str__(self):
        return str(self.post.title)
