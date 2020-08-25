from django.db import models
class RegisterModel(models.Model):
    First_name=models.CharField(max_length=20)
    Last_name=models.CharField(max_length=20)
    Mobile_number=models.IntegerField(unique=True)
    email=models.EmailField()


