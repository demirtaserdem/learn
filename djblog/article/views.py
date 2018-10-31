from django.shortcuts import render,HttpResponse

# Create your views here.
def index(request):
     #return HttpResponse("Anasayfa")
     return render(request,"article/index.html")