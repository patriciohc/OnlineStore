from __future__ import unicode_literals

from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=200)

class Product(models.Model):
	name = models.CharField(max_length=200)
	price = models.DecimalField(max_digits=6, decimal_places=2)
	price_public = models.DecimalField(max_digits=6, decimal_places=2)
	existence = models.IntegerField()
	category = models.ForeignKey(Category, null=True, on_delete=models.CASCADE)
	description = models.CharField(max_length=200, null=True)
	code = models.CharField(max_length=100)
	marca = models.CharField(max_length=200, null=True)
	model = models.CharField(max_length=200, null=True)
	weight = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	ancho = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	largo = models.DecimalField(max_digits=6, decimal_places=2, null=True)
	alto = models.DecimalField(max_digits=6, decimal_places=2, null=True)

class Image(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
	image = models.ImageField(upload_to="image/", null=True)

class Sale(models.Model):
	date_purchase = models.DateTimeField('date purchase')
	tax = models.DecimalField(max_digits=6, decimal_places=2)
	total_plus_tax = models.DecimalField(max_digits=6, decimal_places=2)

class ProductSale(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	sale = models.ForeignKey(Sale, on_delete=models.CASCADE)
	total_products = models.IntegerField()
	tax = models.DecimalField(max_digits=6, decimal_places=2)
	total_plus_tax = models.DecimalField(max_digits=6, decimal_places=2)

class Entrada(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	date_into = models.DateTimeField('date into')
	total_into = models.IntegerField()

class User(models.Model):
	#user = models.ForeignKey()
	purchase = models.ForeignKey(Sale, null=True)
	user_name = models.CharField(max_length=100)
	first_name = models.CharField(max_length=100)
	last_name = models.CharField(max_length=100)
	password = models.CharField(max_length=100, null=True)
	#id_cuente = models.CharField(max_length=100)
	email = models.EmailField()
