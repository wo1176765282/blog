from . import views
from django.urls import path
# from

app_name= 'self'
urlpatterns = [
    path('', views.index,name = 'index'),
    path('<int:con_id>/detail/', views.detail,name = 'detail'),
    path('liuyan/', views.liuyan,name = 'liuyan'),
    path('about/', views.about,name = 'about')
]