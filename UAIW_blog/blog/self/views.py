from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from selfadmin.models import Artical
from pingtai.models import Category
from pingtai.models import Keyword
# from pingtai.models import PTArticle
from util.myutil import authuser

@authuser
def index(request):
    username = request.session.get("username",None)
    id = request.session.get("id",None)
    if request.method =='GET':
        data = Artical.objects.filter(a = id)
        return render(request, 'self/index.html',{'username': username, 'data': data})

# @authuser
def detail(request, con_id):
    con = Artical.objects.filter(id = con_id).first()
    data = Category.getAll()
    random = Artical.objects.order_by('-id')[:2]
    # 推荐
    recommend = Artical.objects.order_by('-id')[:4]
    # article = Artical.getAll()
    keyword = Keyword.objects.all()
    username = request.session.get('username')
    sh = request.session.get('sh')
    return render(request,'self/info.html', {'data':data, 'keyword': keyword, 'username':username,'con':con, 'sh':sh, 'random':random, 'recommend': recommend})

@authuser
def liuyan(request):
    username = request.session.get("username", None)
    if request.method == 'GET':
        return render(request, 'self/liuyan.html', {'username': username})
@authuser
def about(request):
    username = request.session.get("username", None)
    if request.method == 'GET':
        return render(request, 'self/about.html', {'username': username})

