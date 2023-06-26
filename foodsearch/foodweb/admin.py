from django.contrib import admin
from .models import resturants, menus

# Register your models here.
class displayres(admin.ModelAdmin):
    list_display = ['hotel_id', 'hotel_name', 'hotel_location', 'hotel_langitude', 'hotel_longitude'] 
    
class dismenu(admin.ModelAdmin):
    list_display = ['hotel_id', 'food', 'price']
    
admin.site.register(resturants, displayres)
admin.site.register(menus, dismenu)
