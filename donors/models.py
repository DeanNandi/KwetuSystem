from django.db import models


class Donors(models.Model):
    product_name = models.CharField(max_length=250)
    supplier = models.CharField(max_length=250)
    quantity = models.IntegerField()
    recipient = models.CharField(max_length=250)
    employee_id = models.IntegerField()
    date_of_payment = models.CharField(max_length=250)

