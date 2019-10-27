from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Snap(models.Model):
    snap=  models.ImageField(upload_to='images/', blank=True)
    photoname = models.TextField()
    description =models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    
    
    # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    


    def __str__(self):
        return self.snap


    @classmethod
    def search_by_name(cls,search_term):
        searched_user = cls.objects.filter(user__username__contains=search_term)
        return  searched_user
    

    # def save_snap(self):
    #     self.save()

    # def delete_snap(self):
    #     self.delete()

class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField()
    profilepicture= models.ImageField(upload_to='profile/', blank=True)


    def __str__(self):
        return self.profilepicture
