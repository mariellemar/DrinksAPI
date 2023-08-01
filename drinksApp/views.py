from django.shortcuts import render
from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer

def drink_list(request):
    #get all drinks
    #serialize them
    #return json
    
    drinks = Drink.objects.all()
    serliazer = DrinkSerializer(drinks, many=True)
    return JsonResponse({'drinks': serliazer.data}, safe=False)