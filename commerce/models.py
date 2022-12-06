
from django.db import models
from django.utils.text import slugify

class Product(models.Model):
    car_name = models.CharField(max_length=100)
    price = models.CharField( max_length=100, null=True, blank=True)
    author_name = models.CharField(max_length=100,  null=True, blank=True)
    author_number = models.CharField(max_length=100, null=True, blank=True)
    car_accident = models.BooleanField(default=False)
    year_of_manufacture = models.CharField(max_length=15, null=True, blank=True)
    mileage = models.CharField(max_length=64, null=True, blank=True)
    body = models.CharField(max_length=50, null=True, blank=True)
    color = models.CharField(max_length=50, null=True, blank=True)
    equipment = models.CharField(max_length=50, null=True, blank=True)
    condition = models.CharField(max_length=50, null=True, blank=True)
    
    time = models.DateTimeField(auto_now_add=True, )
    mahsulot = models.ForeignKey('Categoriya', on_delete=models.CASCADE, related_name='mahsulot')

    def __str__(self):
        return self.name
class ProductRasmi(models.Model):
    link = models.ImageField(upload_to="media")
    title = models.CharField(max_length=2500, null=True)
    rasmlari = models.ForeignKey('Product', on_delete=models.CASCADE, related_name='rasmlari')
    def __str__(self):
        return self.title


class Categoriya(models.Model):
    category_name = models.CharField(max_length=200)
    
    def __str__(self):
        return self.category_name  
class CategoriyaRasm(models.Model):
    images = models.ImageField(upload_to='media')
    title = models.CharField(max_length=2500, null=True)
    rasmlar = models.ForeignKey('Categoriya', on_delete=models.CASCADE, related_name='rasmlar')
    def __str__(self):
        return self.title
