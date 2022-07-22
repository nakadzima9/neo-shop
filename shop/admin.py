from django.contrib import admin
from .models import CustomUser, Category, Cart, CartItem, Comment, Order, Product

admin.site.register(CustomUser)
admin.site.register(Cart)
admin.site.register(Category)
admin.site.register(CartItem)
admin.site.register(Comment)
admin.site.register(Order)
admin.site.register(Product)
