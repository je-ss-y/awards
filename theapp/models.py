
    
    
    
#     # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    


#     def __str__(self):
#         return self.snap


#     @classmethod
#     def search_by_name(cls,search_term):
#         searched_user = cls.objects.filter(user__username__contains=search_term)
#         return  searched_user
    

#     # def save_snap(self):
#     #     self.save()

#     # def delete_snap(self):
#     #     self.delete()

# class Profile(models.Model):

#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
#     bio = models.TextField()
#     profilepicture= models.ImageField(upload_to='profile/', blank=True)


#     def __str__(self):
#         return self.profilepicture



# class Rating(models.Model):

#     user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
#     creativity = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
#     design = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
#     content = models.IntegerField(choices=list(zip(range(0,11), range(0,11))), default=0)
    


#     def __str__(self):
#         return self.creativity


from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.

class Snap(models.Model):
    image=  models.ImageField(upload_to='images/', blank=True)
    photoname = models.TextField()
    description =models.TextField()
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    pub_date = models.DateTimeField(auto_now_add=True)
    link =  models.URLField(max_length=200)
    # profile = models.ForeignKey(Profile,on_delete=models.CASCADE)

    def __str__(self):
        return self.user

    def save_snap(self):
        self.save()

    @classmethod
    def search_by_name(cls,search_term):
        searched_user = cls.objects.filter(user__username__contains=search_term)
        return  searched_user
    



class Profile(models.Model):

    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
    bio = models.TextField()
    profilepicture= models.ImageField(upload_to='profile/', blank=True)


    def __str__(self):
        return self.bio






