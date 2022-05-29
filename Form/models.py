from django.db import models

# Create your models here.
class UserData(models.Model):
    username=models.CharField(max_length = 500)
    clientname=models.CharField(max_length =500)
    server=models.CharField(max_length =100)
    paymentRecieved=models.CharField(max_length =100)
    paymentType=models.CharField(max_length =100)
    profit=models.CharField(max_length =100)
    date=models.CharField(max_length =100)

    def __str__(self):
        return self.username
        