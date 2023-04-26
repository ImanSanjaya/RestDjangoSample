from django.db import models

# (python manage.py makemigrations home) Perintah untuk Membuat Class Migration
# (python manage.py migrate home) Perintah untuk Membuat class Migration menjadi table di database
# Dan kamu bisa membuat beberapa class untuk pemetaan table di dalam models.py ini

# Create your models here.
class Person(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()