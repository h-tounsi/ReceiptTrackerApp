from django.db import models
from django.contrib.auth.models import User

class Receipt(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE )
    store_name = models.CharField(max_length=100)
    date_of_purchase = models.DateField(null=True, blank=True)
    item_list = models.TextField()
    total_amount = models.IntegerField()
    

    def __str__(self):
        return f'{self.store_name} - {self.date_of_purchase}'

