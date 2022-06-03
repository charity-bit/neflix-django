from django.db import models
from django.contrib.auth.models import User
import uuid
from cloudinary.models import CloudinaryField

# Create your models here.User()


AGE_CHOICES = (
    ('All','All'),
    ('Kids','Kids')
)

MOVIE_CHOICES = (
    ('Series','Series'),
    ('Movie','Movie')
)

# class CustomUser(AbstractUser):
#     profiles = models.ManyToOneRel('Profile',blank=True)


class Profile(models.Model):
    name = models.CharField(max_length=255)
    age_limit = models.CharField(max_length=10,choices = AGE_CHOICES)
    profile_image = CloudinaryField('image',null=True,blank=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    user_id = models.ForeignKey(User,on_delete=models.CASCADE)
