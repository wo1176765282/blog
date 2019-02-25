from . import views
from django.urls import path
# from

app_name= 'pingtai'
urlpatterns = [
    path('', views.index,name = 'index'),
    path('getKeyword/', views.getKeyword, name = 'getKeyword'),
    path('<int:con_id>/detail/', views.detail, name = 'detail'),
    path('kaitong/', views.kaitong, name = 'kaitong'),
    path('yuce/', views.yuce, name = 'yuce')
]