from django.core import validators
from django.db import models
from django.core.validators import MaxValueValidator

class Category(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return f'{self.name}'

class Size(models.Model):

    number = models.PositiveIntegerField(
        validators=[MaxValueValidator(20)]
    )

    def __str__(self):
        return f'Shoe size - {self.number}'

class Shoe(models.Model):

    MALE = 'Male'
    FEMALE = 'Female'
    gender = [
        (MALE,  'Male'),
        (FEMALE, 'Female'),
    ]
    gender = models.CharField(
        max_length=6,
        choices=gender,
        default=MALE
    )

    name = models.CharField(max_length=50)
    category = models.ManyToManyField(
        'category',
        related_name='categories',
        blank=True
    )
    size = models.ManyToManyField(
        'size',
        related_name='size',
        blank=True
    )
    image = models.CharField(max_length=250)
    price = models.PositiveIntegerField(
        validators=[MaxValueValidator(999)]
    )
    colour = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    favourited_by = models.ManyToManyField(
        'jwt_auth.User',
        related_name='favourites',
        blank=True
    )
    in_stock = models.BooleanField()
    owner = models.ForeignKey(
        'jwt_auth.User',
        related_name='owned_stores',
        on_delete=models.CASCADE,
        default=1
    )

    def __str__(self):
        return f'{self.name}'
