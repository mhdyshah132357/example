from rest_framework import serializers
from rest_flex_fields import FlexFieldsModelSerializer

from .models import Product
from .models import Member
from .models import Image
from .models import ProductSize
from .models import Category


from versatileimagefield.serializers import VersatileImageFieldSerializer




class CategorySerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Category
        fields = ['pk', 'name']
        expandable_fields = {
          'products': ('goods.ProductSerializer', {'many': True})
        }




class ProductSizeSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = ProductSize
        fields = ['pk', 'name']






class ProductSerializer(FlexFieldsModelSerializer):
    class Meta:
        model = Product
        fields = ['pk', 'name','created', 'updated' , 'image']
        expandable_fields = {
            'category': ('goods.CategorySerializer', {'many': True}),
            'properties': ('goods.PropertiesSerializer', {'many': True}),
            'image': ('goods.ImageSerializer', {'many': True}),
        }



class MemberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Member
        fields = ('firstname' , 'lastname' , 'password' , 'national_id' , 'birth_date' , 'email' , 'message' , 'zipCode' , 'phoneNumber' , 'address' , 'receivedmoney', 'status' , 'status' , 'access')


class ImageSerializer(FlexFieldsModelSerializer):
    image = VersatileImageFieldSerializer(
        sizes='product_headshot'
    )

    class Meta:
        model = Image
        fields = ['pk', 'name', 'image']