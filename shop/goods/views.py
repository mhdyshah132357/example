from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import generics



from .serializers import ProductSerializer
from .serializers import MemberSerializer
from .serializers import ImageSerializer


from django_filters.rest_framework import DjangoFilterBackend


from rest_flex_fields.views import FlexFieldsModelViewSet , FlexFieldsMixin
from rest_flex_fields import is_expanded


from rest_framework.viewsets import ReadOnlyModelViewSet




from .models import Product
from .models import Member
from .models import Image


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('name')
    serializer_class = ProductSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['price']




class ImageViewSet(FlexFieldsModelViewSet):
    serializer_class = ImageSerializer
    queryset = Image.objects.all()





class MemberViewSet(viewsets.ModelViewSet):
    queryset = Member.objects.all().order_by('lastname')
    serializer_class = MemberSerializer







class APIRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all() 
    serializer_class = ProductSerializer , MemberSerializer