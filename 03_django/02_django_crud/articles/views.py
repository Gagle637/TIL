from IPython import embed
from django.core.exceptions import ValidationError
from django.shortcuts import render, redirect
from .models import Article


# Create your views here.

def index(request):
    # articles = Article.objects.all()
    articles = Article.objects.order_by('-pk') #DB가 변경
    # articles = Article.objects.all()[::-1] #python이 변경
    context = {'articles':articles}
    return render(request, 'articles/index.html', context)

def create(request):
    #CREATE
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        article = Article(title=title, content=content)
        article.save()
        return redirect(article) #메인 페이지
    #NEW
    else:
        return render(request, 'articles/create.html')

    

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    article.get_absolute_url()
    context ={'article': article,}
    return render(request, 'articles/detail.html', context)

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    else:
        redirect(article)

def update(request, pk):
    article = Article.objects.get(pk=pk)
    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        article.save()
        return redirect(article)
    else:
        context = {'article': article}
        return render(request, 'articles/update.html', context)
