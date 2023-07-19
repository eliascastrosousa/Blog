from django.shortcuts import render
import requests 

TMDB_API_KEY = '203bc0d53c6612c9c5e10b6ac1cf9d4d'
url_image = 'https://image.tmdb.org/t/p/original/'

def tvshows(request):
    if request.method == "GET":
        query = request.GET.get('q')

        if query:
            response = requests.get(f"https://api.themoviedb.org/3/search/tv?api_key={TMDB_API_KEY}&language=pt-br&page=1&include_adult=false&query={query}")
            data = response.json()
            search = data['results']
            print(data)
            context = {
                'search': search,
                'url_image' :url_image
            }
            return render(request, 'tvshows.html', context)
        else:

            response = requests.get(f"https://api.themoviedb.org/3/tv/popular?api_key={TMDB_API_KEY}&language=pt-br&page=1")
            data = response.json()
            search = data['results']
            print(data)
            context = {
                'search': search,
                'url_image' :url_image
            }
            return render(request, 'tvshows.html', context)

    return render(request, 'tvshows.html')
        



def movies(request):

    if request.method == "GET":
        query = request.GET.get('q')

        if query:
            response = requests.get(f"https://api.themoviedb.org/3/search/movie?api_key={TMDB_API_KEY}&language=PT-BR&page=1&query={query}")
            data = response.json()
            search = data['results']
            print(data)
            context = {
                'search': search,
                'url_image' :url_image
            }
            return render(request, 'movies.html', context)
        else:
            response = requests.get(f"https://api.themoviedb.org/3/movie/popular?api_key={TMDB_API_KEY}&language=PT-BR&page=1")
            data = response.json()
            search = data['results']
            print(data)
            context = {
                'search': search,
                'url_image' :url_image
            }
            return render(request, 'movies.html', context)
    return render(request, 'movies.html')








