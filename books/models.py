from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator,MinValueValidator


class Book(models.Model):
    title=models.CharField(max_length=200,unique=True)
    description=models.CharField(max_length=300)
    author=models.ForeignKey(User,on_delete=models.CASCADE,related_name='books')
    rating=models.FloatField(default=0,validators=[MaxValueValidator(10),MinValueValidator(1)])
    isbn=models.CharField(max_length=13)
    price=models.DecimalField(max_digits=5,decimal_places=2)

    def __str__(self):
        return self.title
