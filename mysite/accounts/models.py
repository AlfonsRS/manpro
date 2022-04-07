from django.db import models

class Role(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField()
    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    role_id = models.ForeignKey('Role', on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# Create your models here.
