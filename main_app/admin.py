from django.contrib import admin

# Register your models here.

from .models import Hedgehog, Feeding

# Register your models here
admin.site.register(Hedgehog)

admin.site.register(Feeding)