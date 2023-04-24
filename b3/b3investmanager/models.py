import datetime
from django.db import models

# Create your models here.


class Code(models.Model):
    code_identifyer = models.CharField(max_length=6)
    def __str__(self):
        return self.code_identifyer

class Investment(models.Model):
    date = models.DateField("created")
    investment_identifyer = models.CharField(max_length=50, default='no specified')
    Code = models.ForeignKey(Code, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    value_unit = models.DecimalField(max_digits=10, decimal_places=3)
    OPERATIONS = (
        ('C', 'Compra'),
        ('V', 'Venda'),
    )
    operation = models.CharField(max_length=1, choices=OPERATIONS)
    value_brokerage = models.DecimalField(max_digits=10, decimal_places=3)
    value_operation = models.DecimalField(max_digits=10, decimal_places=3)
    b3_rate = models.DecimalField(max_digits=10, decimal_places=3)
    value_total = models.DecimalField(max_digits=10, decimal_places=3)
    def __str__(self):
        return self.investment_identifyer
    
    def was_published_recently(self):
        return self.date >= datetime.timezone.now() - datetime.timedelta(days=1)


    

    
    
