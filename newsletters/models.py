from django.db import models

# Create your models here.
class SignUp(models.Model):
    email = models.EmailField()
    full_name = models.CharField(max_length=120,blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    # for python 2
    def __unicode__(self):
        return self.email

    # for python3
    def __str__(self):
        return self.email