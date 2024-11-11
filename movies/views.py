from django.http import HttpResponse
from django.shortcuts import render
 
data = {
  'movies': [
    {
      'id': 5,
      'title': 'Jaws',
      'year': 2004
    },
    {
      'id': 6,
      'title': 'Constantine',
      'year': 1999
    },
    {
      'id': 8,
      'title': 'Ghost Rider',
      'year': 2001
    }
  ]
}


def movies(request):
  return render(request, 'movies/movies.html', data)

def home(request):
  return HttpResponse("Home Page")