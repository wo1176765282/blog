from django.shortcuts import render,redirect,reverse
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Keyword,Category, PTArticle, UserInfo
from userauth.models import User
from selfadmin.models import Artical
from .forms import UserInfoFrom
from django.db import models
from gensim import corpora,models,similarities
import jieba
from django.db import connection
# Create your views here.

def dictfetchall(cursor):
    "将游标返回的结果保存到一个字典对象中"
    desc = cursor.description
    return [dict(zip([col[0] for col in desc], row)) for row in cursor.fetchall() ]

def index(request):
    if request.method == 'GET':
        c = request.GET.get("c",None)
        keyword = request.GET.get("keyword", None)
        # 关键字筛选
        if not c:
            if not keyword:
                article = PTArticle.getAll()
                article1 = Artical.objects.all()
            else:
                keyword = int(keyword)
                article = PTArticle.objects.filter(k_id = keyword)
                article1 = Artical.objects.filter(k_id = keyword)
        else:
            c = int(c)
            article = PTArticle.objects.filter(c_id=c)
            article1 = Artical.objects.filter(c_id=c)
        data = Category.getAll()
        random = PTArticle.objects.order_by('-id')[:2]
        keyword = Keyword.objects.all()
        username = request.session.get('username',None)
        recommend = []
        # cursor = connection.cursor()
        # 推荐内容
        if username:
            a = User.objects.filter(username = username).first()
            user_artical = Artical.objects.filter(a = a.id).all()
            all_artical = Artical.objects.filter().exclude(a = a.id)
            if user_artical:
                all_doc_list = []
                for doc in user_artical:
                    doc_list = [word for word in jieba.cut(doc.title)]
                    all_doc_list.append(doc_list)
                all_test_list = []
                for doc in all_artical:
                    doc_list = [word for word in jieba.cut(doc.title)]
                    all_test_list.append(doc_list)
                # 获取词袋
                dictionary = corpora.Dictionary(all_doc_list)
                # 词袋中用数字对所有词进行编号
                # dictionary.keys()
                #dictionary.token2id  # 查看编号与词之间的关系
                # 用doc2bow制作语料库  语料库是一组向量   二元组【编号，频次数】
                corpus = [dictionary.doc2bow(doc) for doc in all_doc_list]
                # 测试文档转换为二元组的向量
                doc_test_vec = [dictionary.doc2bow(doc) for doc in all_test_list]
                # 使用TF - IDF模型对语料库建模
                tfidf = models.TfidfModel(corpus)
                print(tfidf[doc_test_vec])  #获取测试文档中，每个词的TF-IDF值
                index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=len(dictionary.keys()))
                for i in range(len(doc_test_vec)):
                    sim = index[tfidf[doc_test_vec[i]]]
                    # 根据相似度排序
                    if len(sorted(enumerate(sim), key=lambda item: -item[1]))>=4:
                        for j in range(4):
                            recommend.append(all_artical[sorted(enumerate(sim), key=lambda item: -item[1])[j][0]])
                    else:
                        recommend = Artical.objects.order_by('-id')[:4]

        else:
            recommend = Artical.objects.order_by('-id')[:4]
            # cursor.execute('select id,title from selfadmin_artical order by id desc limit 4')
            # result = dictfetchall(cursor)
            # recommend.append(result)
        sh = request.session.get('sh')
        return render(request,'pingtai/index.html', {'data': data, 'article': article,  'article1': article1, 'keyword': keyword,'username': username, 'sh':sh, 'random':random, 'recommend': recommend})


# ajax跨域请求
@csrf_exempt
def getKeyword(request):
    if request.is_ajax():
        c = request.POST.get('c',None)
        res = Keyword.objects.filter(c=c).values_list('id','name')
        obj = {}
        for arr in res:
            obj[arr[0]] = arr[1]
        return JsonResponse(obj)
# 文章内容页
def detail(request, con_id):
    con = Artical.objects.filter(id = con_id).first()
    a_id = con.a_id
    all_article = Artical.objects.filter(a_id = a_id).all()

    data = Category.getAll()
    random = PTArticle.objects.order_by('-id')[:2]
    # 推荐
    recommend = PTArticle.objects.order_by('-id')[:4]
    keyword = Keyword.objects.all()
    username = request.session.get('username')
    sh = request.session.get('sh')
    return render(request,'pingtai/info.html', {'data':data, 'keyword': keyword, 'username':username,'con':con, 'sh':sh, 'random':random, 'recommend': recommend, 'all_article':all_article})

# 开通博客
def kaitong(request):
    if request.method=='GET':
        username = request.session.get('username',None)
        # sh = request.session.get('sh',None)
        if username:
            # 判断是否为普通用户  高级用户进入到自己的博客
            obj = User.objects.filter(username=username).first()
            if int(obj.c) == 0:
                form = UserInfoFrom()
                return render(request,'pingtai/kaitong.html', {'form': form})
            else:
                return render(request,'用户后台')
        else:
            return redirect(reverse("userauth:login"))
    else:
        form = UserInfoFrom(request.POST)
        if form.is_valid():
            # 后台管理员做验证，是否通过验证
            id = request.session.get('id')
            data = form.cleaned_data
            UserInfo.objects.create(company=data['company'], position=data['position'], reason=data['reason'], hobby=data['hobby'], realname=data['realname'], u_id= id)
            User.objects.filter(id=id).update(sh=1)
            request.session['sh'] = 1
            return redirect(reverse('pingtai:index'))
        else:
            # 返回开通页面
            username = request.session.get('username', None)
            if username:
                # 判断是否为普通用户  高级用户进入到自己的博客
                obj = User.objects.filter(username=username).first()
                c = obj.c
                if int(c) == 0:
                    # form = UserInfo.objects.filter(u=obj.id)
                    return render(request, 'pingtai/kaitong.html')

# 房价预测
def yuce(request):
    if request.method == 'GET':
        return render(request,'pingtai/yuce.html')
    else:
        qu = request.POST.get('qu')
        shi = request.POST.get('shi')
        ting = request.POST.get('ting')
        area = request.POST.get('area')
        ceng = request.POST.get('ceng')
        subway = request.POST.get('subway')
        school = request.POST.get('school')
        import numpy as np
        from .yuce import pre
        data = np.array([0 for i in range(12)]).reshape(1,-1)
        data[0][0]=shi
        data[0][1]=ting
        data[0][2]=area
        data[0][3]=subway
        data[0][4]=school
        if qu == 'haidian':
            data[0][5]=1
        elif qu == 'fengtai':
            data[0][6] = 1
        elif qu == 'xihceng':
            data[0][7]=1
        elif qu == 'dongcheng':
            data[0][8]=1
        elif qu == 'shijingshan':
            data[0][9]=1
        if ceng == 'middle':
            data[0][10]=1
        elif ceng =='high':
            data[0][11]=1
        # [roomnum, halls, area, subway, school, 1, 0, 0, 0, 0] + floors)[0]
        pres = pre(data)[0]
        pres = np.round(pres,2)
        return render(request,'pingtai/yuce.html',{'pres' : pres})