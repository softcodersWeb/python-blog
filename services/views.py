from django.shortcuts import render

# Create your views here.
def services(request):
  return render(request, "articles/services.html")