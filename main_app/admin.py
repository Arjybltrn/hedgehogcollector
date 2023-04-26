from django.contrib import admin

# Register your models here.

from .models import Hedgehog, Feeding, Toy

# Register your models here
admin.site.register(Hedgehog)

admin.site.register(Feeding)

admin.site.register(Toy)