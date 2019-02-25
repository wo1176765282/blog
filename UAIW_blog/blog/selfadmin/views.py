from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from pingtai.models import UserInfo,User,Category,Keyword
from userauth.models import User as Us
from util.myutil import authuser
from django.views.decorators.csrf import csrf_exempt
import os,time
from .forms import AddArticleForm
from .models import Artical

@authuser
def personal(request):
    username = request.session.get("username", None)
    if request.method == 'GET':
        form = User.objects.filter(username=username).first()
        # print(form.userinfo.hobby)
        return render(request, 'selfadmin/personal.html', {'username': username, 'form': form})

@csrf_exempt
@authuser
def EditPersonal(request):
    username = request.session.get("username", None)
    if request.method == 'GET':
        form = User.objects.filter(username=username).first()
        # print(form.userinfo.hobby)
        return render(request, 'selfadmin/EditPersonal.html', {'username': username, 'form': form})
    else:
        realname = request.POST.get('realname')
        password = request.POST.get('password')
        tel = request.POST.get('tel')
        email = request.POST.get('email')
        position = request.POST.get('position')
        company = request.POST.get('company')
        hobby = request.POST.get('hobby')
        u_id = User.objects.filter(username=username).first().id
        User.objects.filter(username=username).update(tel=tel, email=email, password=password)
        UserInfo.objects.filter(u_id=u_id).update(position=position, company=company,hobby=hobby, realname=realname)
        return redirect(reverse('selfadmin:personal'))


@csrf_exempt
def upload(request):
    username = request.session.get("username", None)
    if request.is_ajax():
        img = request.FILES.get('img',None)
        name = os.path.join('uploads', 'user_img', img.name)
        if img:
            with open(name, 'wb+') as f:
                for i in img.chunks():
                    f.write(i)
        User.objects.filter(username=username).update(img=os.path.join('user_img', img.name))
        return JsonResponse({'status': 'ok', 'src': '/media/user_img/%s'%img.name})

def article(request):
    username = request.session.get("username", None)
    if request.method == 'GET':
        form = User.objects.filter(username=username).first()
        obj = Us.objects.filter(username=username).first()
        category = Category.objects.all()
        keyword = Keyword.objects.all()
        articles = obj.artical_set.all()
        c1=request.GET.get('c1',None)
        k1=request.GET.get('k1',None)
        s1=request.GET.get('status1',None)

        # 先判断c1
        if c1:
            keys = Keyword.objects.filter(c_id=c1)
            if k1:
                if s1:
                    articles = Us.objects.filter(username=username).first().artical_set.filter(c_id=c1, k_id=k1, status=s1)
                else:
                    articles = Us.objects.filter(username=username).first().artical_set.filter(c_id=c1, k_id=k1)
            else:
                if s1:
                    articles = Us.objects.filter(username=username).first().artical_set.filter(c_id=c1, status=s1)
                else:
                    articles = Us.objects.filter(username=username).first().artical_set.filter(c_id=c1)
        else:
            keys = Keyword.objects.all()
            if k1:
                if s1:
                    articles = Us.objects.filter(username=username).first().artical_set.filter(k_id=k1, status=s1)
                else:
                    articles = Us.objects.filter(username=username).first().artical_set.filter(k_id=k1)
            else:
                if s1:
                    articles = Us.objects.filter(username=username).first().artical_set.filter(status=s1)
                else:
                    articles = Us.objects.filter(username=username).first().artical_set.all()
        if c1:
            c1 = int(c1)
        if k1:
            k1 = int(k1)

        return render(request, 'selfadmin/article.html', {'username': username, 'form': form, 'articles':articles, 'category':category, 'keyword':keyword, 'c1':c1, 'k1':k1, 's1': s1})

@authuser
def AddArticle(request):
    username = request.session.get("username", None)
    if request.method == 'GET':
        forms = AddArticleForm()
        form = User.objects.filter(username=username).first()
        return render(request, 'selfadmin/AddArticle.html', {'username': username, 'form': form, 'forms': forms})
    else:
        forms = AddArticleForm(request.POST)
        if forms.is_valid():
            obj = forms.save(commit=False)
            print(obj)
            obj.a = Us.objects.filter(username= username).first()
            obj.save()
        form = User.objects.filter(username=username).first()
        forms = AddArticleForm()
        return render(request, 'selfadmin/AddArticle.html', {'username': username, 'form': form, 'forms': forms})

def MyConcern(request):
    pass

def MyFans(request):
    pass

