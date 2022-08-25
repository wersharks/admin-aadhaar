from django.db import models

class Operator(models.Model):
    # name = models.CharField(max_length=100)
    # phoneNo = models.CharField(max_length=20)
    # email = models.EmailField(max_length=100)
    picture = models.ImageField(upload_to='pics', default = 'img/default-avatar.png')

def __str__(self):
     return self.title