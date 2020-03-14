from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Stock
from .forms import StockForm
# Create your views here.

def home(request):
    if request.method == "POST":
        import requests
        import json
        
        #pk_4335e55ab8444511a9ad95399164cb69
        symbol = request.POST['query']
        api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token=pk_4335e55ab8444511a9ad95399164cb69")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error"
        
        return render(request, 'home.html', {'api' : api,})


    else:
        return render(request, 'home.html')



def stock(request):
    if request.method == "POST":
        form = StockForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, 'successfully, added new ticker!')
        else:
            messages.success(request, 'could not add your ticker, please try gain!')

        return redirect('stock')

    else:
        import requests
        import json

        symbols = Stock.objects.all()
        tickers = []
        for symbol in symbols:
            api_request = requests.get(f"https://cloud.iexapis.com/stable/stock/{symbol}/quote?token=pk_4335e55ab8444511a9ad95399164cb69")      
            #api = json.loads(api_request.content)
            try:
                api = json.loads(api_request.content)
                tickers.append(api)
            except Exception as e:
                api = "Error"
        

        return render(request, 'stock.html', {'tickers' : tickers})
