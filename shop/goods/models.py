from django.db import models 
from django.utils import timezone
from datetime import date
from versatileimagefield.fields import VersatileImageField , PPOIField


class ProductSize(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

        

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name




class Image(models.Model):
    name = models.CharField(max_length=255)
    image = VersatileImageField(
        'Image',
        upload_to='images/',
        ppoi_field='image_ppoi'
    )
    image_ppoi = PPOIField()

    def __str__(self):
        return self.name


        

class Product(models.Model):
    name = models.CharField(max_length = 250)
    price = models.FloatField(blank = True , null = True)
    category = models.ManyToManyField(Category, related_name='products')
    properties = models.CharField(max_length = 300)
    created = models.DateField(auto_now_add=True , null=True)
    updated = models.DateField(auto_now=True , null=True)
    image = models.ManyToManyField('goods.Image', related_name='products')
    
    
    class Meta:
        ordering = ['created']



    def __str__(self):
        return self.name





class Member(models.Model):
    firstname = models.CharField(max_length=100 , default='', null = True)
    lastname = models.CharField(max_length=100, null = True)
    password = models.CharField(max_length=100 , null = True)
    national_id = models.IntegerField(null = True)
    birth_date = models.DateTimeField(help_text='Enter number of your birth' , null = True , blank = True)
    email = models.EmailField(null = True)
    message = models.CharField(max_length=400 ,null = True , blank = True)
    zipCode = models.CharField(max_length=100, null = True)
    phoneNumber = models.CharField(max_length=100, null = True)
    address = models.TextField(max_length=10000, null = True)
    receivedmoney = models.IntegerField(blank=True , null=True)
    #product = models.ForeignKey('Product' , on_delete = models.SET_NULL , null = True)

    LOAN_STATUS = (
        ('a','Activate'),         
        ('s','Staff status'),
        ('u','Supperuser status'),
    )

    access = models.CharField (max_length= 10 , choices= LOAN_STATUS , blank= True , default= 'a' , help_text='enter the accessibility')

    ACCESS_STATUS = (
        ('green','Green'),
        ('yellow','Yellow'),
        ('red','Red'),
        ('gray','Gray'),
    )

    status = models.CharField(max_length=10 , choices= ACCESS_STATUS , blank=True , default='y' , help_text='enter the  status by colors')


    def __str__(self):
        return self.firstname

