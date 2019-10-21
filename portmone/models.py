from django.db import models


class PortmonePayment(models.Model):

    created = models.DateTimeField(auto_now=True)
    shopOrderNumber = models.CharField(unique=True, editable=False, max_length=255)

    def __str__(self):
        return 'Portmone payment (shopOrderNumber: {})'.format(self.shopOrderNumber)
