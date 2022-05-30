from django.shortcuts import render
from django.http  import HttpResponse
from .models import Category,Location,Image

# Create your views here.
def welcome(request):
    return render(request, 'index.html')
    
def images(request):
    images = Image.objects.all()
    category = Category.objects.all()
    location = Location.objects.all()
    return render(request,'images.html',{'images':images,'category':category,'location':location})
def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET["category"]
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":images,"images": searched_images})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})    

