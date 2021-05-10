from django.contrib import admin


from .models import Product
from .models import Member
from .models import Image
from .models import ProductSize
from .models import Category





admin.site.register(ProductSize)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Member)
admin.site.register(Image)

admin.site.site_header = "Product Goods Admin"
