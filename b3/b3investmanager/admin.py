from django.contrib import admin

# Register your models here.
from .models import  Investment, Code

admin.site.register(Investment)
admin.site.register(Code)