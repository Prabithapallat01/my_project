from django.db import models

# Create your models here.
class Brands(models.Model):
    brand_name=models.CharField(max_length=120,unique=True)

    def __str__(self):
        return self.brand_name

class Mobile(models.Model):
    mobile_name=models.CharField(max_length=120)
    brand=models.ForeignKey(Brands,on_delete=models.CASCADE)
    price = models.IntegerField(null=False)
    model_name = models.CharField(max_length=120,default='')
    specs = models.CharField(max_length=120,default='')
    desciption = models.CharField(max_length=120,default='')
    img=models.ImageField(upload_to='images',default='')
    #,default='',blank=True,null=True


    def __str__(self):
        return self.mobile_name

class Orders(models.Model):

    product=models.ForeignKey(Mobile,on_delete=models.CASCADE)
    DeliveryAddress=models.CharField(max_length=230)
    user=models.CharField(max_length=120)
    choices=[
        ("ordered","ordered"),
        ("dispatched","dispatched"),
        ("cancelled","cancelled")
    ]
    status=models.CharField(max_length=10,choices=choices,default='ordered')

    def __str__(self):
        return self.user


