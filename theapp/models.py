from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# class Snap(models.Model):
#     snap=  models.ImageField(upload_to='images/', blank=True)
#     photoname = models.TextField()
#     photoname = models.TextField()
#     # upvote = models.ManyToManyField(User)
#     user = models.ForeignKey(User,on_delete=models.CASCADE)
#     pub_date = models.DateTimeField(auto_now_add=True)
    
#     # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

#     # tags = models.ManyToManyField(tags)


#     def __str__(self):
#         return self.snap

    # def save_snap(self):
    #     self.save()

    # def delete_snap(self):
    #     self.delete()