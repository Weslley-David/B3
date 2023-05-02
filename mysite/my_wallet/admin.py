from django.contrib import admin

# Register your models here.

from .models import Investidor, Stock, Transaction

admin.site.register(Investidor)
admin.site.register(Stock)
admin.site.register(Transaction)