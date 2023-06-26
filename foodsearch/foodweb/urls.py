from django.urls import path
from . import views 

app_name = "Foodweb"
urlpatterns = [
    path('', views.search, name="Search"), 
    path('allresturants', views.resturant, name="allResturant"),  
    path('<str:menu_id>/menu', views.resturantmenu, name="Menu"),   
]
