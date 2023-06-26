from django.shortcuts import render, get_object_or_404
from .models import menus, resturants

# Create your views here.
def resturantmenu(request, menu_id): 
    menu = get_object_or_404(resturants, hotel_id=menu_id) #
    context = {
        "menu": menu, 
    }
    return render(request, 'foodweb/mainpage.html', context) 

def search(request):
    query = request.GET.get('query') 
    dishes = menus.objects.filter(food=query) if query else []
    context= {
        'query': query,
        'dishes': dishes,
    }
    return render(request, 'foodweb/search.html', context) 


def resturant(request):
    res = resturants.objects.all()
    context = {
        'res' : res,
    } 
    return render(request, "foodweb/resturant.html", context) 
