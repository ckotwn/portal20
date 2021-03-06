from django.shortcuts import render
from django.http import HttpResponse

from apps.data.models import DataSet
from apps.article.models import Article

def index(request):

    news_list = Article.objects.filter(category='NEWS').all()[0:4]
    event_list = Article.objects.filter(category='EVENT').all()[0:4]
    update_list = Article.objects.filter(category='UPDATE').all()[0:4]
    topic_list = Article.objects.filter(category__in=['SCI', 'TECH', 'PUB']).order_by('?').all()[0:10]
    context = {
        'news_list': news_list,
        'event_list': event_list,
        'update_list': update_list,
        'topic_list': topic_list
    }
    return render(request, 'index.html', context)

def publishing_data(request):
    return render(request, 'publishing-data.html')

def journals(request):
    return render(request, 'journals.html')

def cookbook(request):
    return render(request, 'cookbook.html')

def cookbook_detail_1(request):
    return render(request, 'cookbook-detail-1.html')

def cookbook_detail_2(request):
    return render(request, 'cookbook-detail-2.html')

def cookbook_detail_3(request):
    return render(request, 'cookbook-detail-3.html')

def tools(request):
    return render(request, 'tools.html')

def contact_us(request):
    return render(request, 'contact-us.html')

def plans(request):
    return render(request, 'plans.html')

def links(request):
    return render(request, 'links.html')

def about_taibif(request):
    return render(request, 'about-taibif.html')

def about_gbif(request):
    return render(request, 'about-gbif.html')

def open_data(request):
    return render(request, 'open-data.html')

def data_stats(request):
    is_most = request.GET.get('most', '')
    query = DataSet.objects
    if is_most:
        query = query.filter(is_most_project=True)
    context = {
        'dataset_list': query.all()
    }
    return render(request, 'data-stats.html', context)
