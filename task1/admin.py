from django.contrib import admin

# Register your models here.
from .models import counter

admin.site.register(counter)
