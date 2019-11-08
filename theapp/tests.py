from django.test import TestCase
from .models import *


class SnapTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Snap(user = 'James',photoname = 'mypic', description ='Muriuki', link ='link.github', image ='img.png')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Snap))



    # Testing Save Method
    def test_save_method(self):
        self.james.save_user()
        users = Snap.objects.all()
        self.assertTrue(len(users) > 0)

     # Testing Save Method
    def test_delete_method(self):
        self.james.delete_editor()
        users = Snap.objects.all()
        self.assertTrue(len(users) ==0)

class ProfileTestClass(TestCase):

    # Set up method
    def setUp(self):
        self.james= Profile(user = 'James', bio ='Muriuki', profilepicture ='img.png')

    # Testing  instance
    def test_instance(self):
        self.assertTrue(isinstance(self.james,Profile))



    # Testing Save Method
    def test_save_method(self):
        self.james.save_profile()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) > 0)

     # Testing Save Method
    def test_delete_method(self):
        self.james.delete_editor()
        profiles = Profile.objects.all()
        self.assertTrue(len(profiles) ==0)