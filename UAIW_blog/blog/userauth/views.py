from django.shortcuts import render,reverse,redirect
from django.http import HttpResponse,JsonResponse
from .forms import RegisterForm,LoginForm
from .models import User
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
@csrf_exempt
def login(request):
    if request.method == 'GET':
        form = LoginForm()
        return render(request,"userauth/login.html", {'form':form})
    else:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            id = User.objects.filter(username=username).first().id
            sh = User.objects.filter(username=username).first().sh
            request.session['username'] = username
            request.session['id'] = id
            request.session['sh'] = sh
            return redirect(reverse('pingtai:index'))
        return render(request, 'userauth/login.html', {'form':form})


@csrf_exempt
def register(request):
    if request.method == 'GET':
        forms = RegisterForm()
        return render(request,"userauth/register.html",{'forms':forms})
    else:
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            # 跳转
            return redirect(reverse('userauth:login'),{'forms':form})
        else:
            return render(request,"userauth/register.html",{'forms':form})

def logout(request):
    if request.method=='GET':
        username = request.session.get('username',None)
        if username:
            del request.session['username']
            del request.session['id']
            del request.session['sh']
        return redirect(reverse('userauth:login'))
