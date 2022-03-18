from django.shortcuts import render

def alemeno_home_view(request):
  return render(request, 'alemeno/homepage.html')
