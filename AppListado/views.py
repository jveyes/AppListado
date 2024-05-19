from django.shortcuts import render
from .models import Users, Remates
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
#from django.views.decorators.cache import cache_page

# PAGINA --> index.html
def index(request):
    return render(request, 'index.html')

# PAGINA --> testdb.html
def testdb(request):
    query = request.GET.get('q')
    if query:
        users = Users.objects.filter(username__icontains=query)
    else:
        users = Users.objects.all()
    
    paginator = Paginator(users, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'testdb.html', {'users': page_obj})

#@cache_page(60*15)
def applistado(request):
    query = request.GET.get('q')
    if query:
        remates = Remates.objects.filter(username__icontains=query)
    else:
        remates = Remates.objects.all()
    
    paginator = Paginator(remates, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'applistado.html', {'remates': page_obj})

""" # PAGINA --> mysql.html
def mysql(request):
    users = Users.objects.all()

    users_per_page = 15
    paginator = Paginator(users, users_per_page)

    page = request.GET.get('page')
    try:
        users = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        users = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        users = paginator.page(paginator.num_pages)

    return render(request, 'mysql.html', {'users': users}) """

# DATABASE REMOTE SERVER
#def mysql(request):
#    users = Users.objects.all()
#    return render(request, 'mysql.html', {'users': users})
