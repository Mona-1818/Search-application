from django.db import models 

# Create your models here.

class resturants(models.Model): 
    hotel_id = models.BigIntegerField()
    hotel_name = models.CharField(max_length= 200)  
    # hotels_name = models.CharField(max_length= 200) 
    hotel_location = models.CharField(max_length=200)
    hotel_langitude = models.CharField(max_length=200)
    hotel_longitude = models.CharField(max_length=200) 
    
    def __str__(self) -> str:
        return str(self.hotel_id)

class menus(models.Model):
    hotel_id = models.ForeignKey(resturants, on_delete=models.CASCADE)
    food = models.CharField(max_length=200)
    price = models.CharField(max_length=100)
    
    def __str__(self):
        return self.food
    
# to scrape data points form given csv file 
# from .scrap import Command    
# obj = Command()
# obj.handle()    