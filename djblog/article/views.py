from django.shortcuts import render,HttpResponse,redirect
from .forms import ArticleForm
from django.contrib import messages
from .models import Article
# Create your views here.
def index(request):
    context = {
        "numbers" : [1,2,3,4,5,6]
    }
     #return HttpResponse("Anasayfa")
     #return render(request,"index.html",{"number":"1"})
    return render(request,"index.html",context)


def about(request):
    return render(request,"about.html")

def dashboard(request):
    articles = Article.objects.filter(author = request.user)
    context = {
        "articles": articles
    }
    return render(request,"dashboard.html",context)

def addArticle(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save(commit = False)
        article.author = request.user
        article.save()
        """
        article objesi
        article.save()
        """
        messages.success(request,"Makale Başarıyla Oluşturuldu")
        return redirect("index")
    return render(request,"addarticle.html",{"form" : form})

def detail(request,id):
    article = Article.objects.filter(id = id).first()
    return render(request,"detail.html",{"article":article})
