from django.shortcuts import render
from django.http import HttpResponse
import requests

def home_view(request):
    url = 'https://api.coingecko.com/api/v3/coins/markets?vs_currency=USD&order=market_cap_desc&per_page=100&page=1&sparkline=false'
    data = requests.get(url).json()

   # return HttpResponse(data)

    context = {'data': data}
    return render(request, 'positions/main.html', context)
