from django.shortcuts import render

# Create your views here.

def home(request):
    import requests
    import json
    
    #pk_4335e55ab8444511a9ad95399164cb69
    api_request = requests.get("https://cloud.iexapis.com/stable/stock/aapl/quote?token=pk_4335e55ab8444511a9ad95399164cb69")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error"
    
    return render(request, 'home.html', {'api' : api,})
