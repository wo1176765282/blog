from . import views
from django.urls import path
# from

app_name= 'selfadmin'
urlpatterns = [
    # path('', views.index, name = 'index'),
    path('personal/', views.personal, name = 'personal'),
    path('EditPersonal/', views.EditPersonal, name = 'EditPersonal'),
    path('article/', views.article,name = 'article'),
    path('AddArticle/', views.AddArticle,name = 'AddArticle'),
    path('MyConcern/', views.MyConcern,name = 'MyConcern'),
    path('MyFans/', views.MyFans,name = 'MyFans'),
    path('upload/', views.upload,name = 'upload'),
]