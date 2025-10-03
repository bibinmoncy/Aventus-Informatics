
from django.db import models

class Employee(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    photo = models.ImageField(upload_to='photos/', null=True, blank=True)
    age = models.IntegerField(null=True, blank=True)
    department = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} <{self.email}>"

