from django.shortcuts import render

def home_page(request):
    # 'render' tells Django to combine the request with the HTML template file
    return render(request, 'home.html')