from django.contrib import admin

# Register your models here.
from cart.models import items, cartlist

admin.site.register(cartlist)
admin.site.register(items)
