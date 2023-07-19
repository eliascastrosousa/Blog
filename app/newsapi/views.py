from django.shortcuts import render
import requests
from datetime import datetime, timedelta

API_KEY = '959f0ea6c71c4be4aa4c62880034cd9a'

def news(request):
    hoje = datetime.today()
    print("#### HOJE: ",hoje)
    mes_anterior = hoje - timedelta(days=30)
    print("##### Mês anterior: ", mes_anterior)
    data_formatada = mes_anterior.strftime('%Y-%m-%d')
    print("###### DATA MÊS ANTERIOR: ",data_formatada)

    if request.method == "GET":
        query = request.GET.get('q')
        if query:
            url = f'https://newsapi.org/v2/everything?q={query}&domains=jovemnerd.com.br,olhardigital.com.br,ign.com,terra.com.br,cinepop.com.br&from={str(data_formatada)}&language=pt&sortBy=popularity&apiKey={API_KEY}'

            response = requests.get(url)
            data = response.json()
            articles = data['articles']
            context = {
                'articles': articles
            }
            return render(request, 'news.html', context)
        else:
            query = 'movies'
            url = f'https://newsapi.org/v2/everything?q={query}&domains=jovemnerd.com.br,olhardigital.com.br,ign.com,terra.com.br,cinepop.com.br&from={str(data_formatada)}&language=pt&sortBy=popularity&apiKey={API_KEY}'

            response = requests.get(url)
            data = response.json()
            articles = data['articles']
            context = {
                'articles': articles
            }
            return render(request, 'news.html', context)


    
