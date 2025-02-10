from django.db import models

class Customer(models.Model):
    customer_id = models.CharField(max_length=50, primary_key= True)
    customer_name = models.CharField(max_length=50)
    customer_create_at = models.DateField(auto_now_add= True)
    customer_tell = models.CharField(max_length=50)
