from django.db import models
from django.contrib.auth.models import User

class Product(models.Model):

    # user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True)
    name = models.CharField(max_length=50)
    egprice = models.FloatField( )
    usdprice = models.FloatField( )
    uroprice = models.FloatField( )
    image_url = models.CharField(max_length=500)


    def __str__(self):
        """String for representing the MyModelName object (in Admin site etc.)"""    
        return self.name
