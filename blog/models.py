from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

# Create your models here.
class Blog(models.Model):
    sno=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255)
    slug=models.CharField(max_length=130)
    views=models.IntegerField(default=0)
    timeStamp=models.DateTimeField(blank=True)
    blog = models.ImageField(upload_to="blog/img", default="")
    content=models.TextField()

    def __str__(self):
      return self.title 

class BlogComment(models.Model):
    sno= models.AutoField(primary_key=True)
    comment=models.TextField()
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    post=models.ForeignKey(Blog, on_delete=models.CASCADE)
    parent=models.ForeignKey('self',on_delete=models.CASCADE, null=True )
    timestamp= models.DateTimeField(default=now) 

    def __str__(self):
        return self.comment[0:13] + "..." + "by" + " " + self.user.username