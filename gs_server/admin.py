from django.contrib import admin
from .models import Shoe, Category, Size
# admin
admin.site.register(Shoe)
admin.site.register(Category)
admin.site.register(Size)
