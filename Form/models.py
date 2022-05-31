from django.db import models

# Create your models here.
class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    username=models.CharField(max_length = 500)
    clientname=models.CharField(max_length =500)
    server=models.CharField(max_length =100)
    paymentRecieved=models.CharField(max_length =100)
    paymentType=models.CharField(max_length =100)
    transaction=models.CharField(max_length =100,default='')
    sellAmount=models.CharField(max_length =100,default='')
    buyAmount=models.CharField(max_length =100,default='')
    phone=models.CharField(max_length =100,default='')
    # profit=models.CharField(max_length =100)
    date=models.CharField(max_length =100)

    def __str__(self):
        return self.username
        