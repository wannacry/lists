from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

from moviesapp.models import Movie
from .profile_img_generation import profile_img_generator
# Create your models here.


CHOISES = [
    ('male','Male'),
    ('female','Female'),
    ('not_defined','Not defined'),
]
class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)
    profile_img = models.ImageField(upload_to='static/profile_img/')
    about_info = models.TextField(max_length=1000, blank=True,null=True)
    sex = models.CharField(max_length=12, choices=CHOISES,default='not_defined')

    def save(self,*args,**kwargs):
        if not self.profile_img:
            self.profile_img = profile_img_generator(self.user.username,self.user.email)
        super().save(*args, **kwargs)


@receiver(post_save,sender=User)
def create_profile(sender,instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    if hasattr(instance,'profile'):
        instance.profile.save()

CHOISES = [
    ('planned','Planned'),
    ('viewed','Viewed'),
    ('abandoned','Abandoned'),
    ('postponed','Postponed'),
]

class MoviesList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    film_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    list_status = models.CharField(max_length=12, choices=CHOISES,default='not_defined')
    date_added = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.user}+{self.film_id}+{self.list_status}'


