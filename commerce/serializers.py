
from asyncore import read
from rest_framework import serializers
from .models import *

class ProductRasmiSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductRasmi
        fields = ['id', 'title', 'link', 'rasmlari']
class ProductSerializer(serializers.ModelSerializer):
    rasmlari = ProductRasmiSerializer(many= True, read_only=True)
    class Meta: 
        model = Product
        fields = ['id', 'car_name', 'price', 'author_name', 'author_number', 'car_accident', 'year_of_manufacture', 'mileage', 'body', 'color', 'equipment', 'condition' ,'time',  'mahsulot', 'rasmlari']
    def __str__(self):
        return self.nomi


class FileSerializer(serializers.ModelSerializer):
    class Meta:
        model = CategoriyaRasm
        fields = ['id', 'images', 'title', 'rasmlar']


class CategorySerializer(serializers.ModelSerializer):
    # category = MassageSerializer(many=True, read_only=True)
    rasmlar= FileSerializer(many= True, read_only=True)
    mahsulot = ProductSerializer(many=True, read_only=True)
    class Meta:
        model = Categoriya
        fields = ['id','category_name', 'rasmlar', 'mahsulot' ]