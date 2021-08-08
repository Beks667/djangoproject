from django.shortcuts import render,get_object_or_404,HttpResponse
from .models import News
# Create your views here.

def news(request):
    news = News.objects.all()
    return render(request,'news/news.html',
    {'all_news':news})

def news_detail(request,pk):
    one_news =get_object_or_404(News,pk=pk)
    return 


