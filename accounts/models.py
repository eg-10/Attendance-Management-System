from django.db import models
from django.contrib.auth.models import User


class Student(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE)
    uid = models.CharField(max_length=200)
    attendance = models.CharField(blank=True, null=True, max_length=200)

    def __str__(self):
        return self.uid + ':' + self.user.first_name + ' ' + self.user.last_name
