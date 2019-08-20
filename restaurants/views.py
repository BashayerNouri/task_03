from django.shortcuts import render

def welcome(request):
    return render(request, 'index.html', {'msg':'Hello World!'})

def restaurant_list(request):

    context = {
    "my_list": [ 
    {"restaurant_name": "Babel", "food_type": "Lebanese",},
    {"restaurant_name": "Mais Al Ghanim", "food_type": "Lebanese",},
    {"restaurant_name": "Fridays", "food_type": "American",},
    ],

    }
    return render(request, 'list.html', context)


def restaurant_detail(request):

    context = {

    "my_object": {

    "restaurant_name": "Babel", 
    "food_type": "Lebanese",
    
    }, 

    }
    return render(request, 'detail.html', context)
