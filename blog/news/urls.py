from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.index,name='index'),
    path('advertise/',views.advert, name='advertise'),
    path('about/',views.about, name='about'),
    path('details/<str:slug>/', views.detail,name='details'),
    path('detailsTrend/<str:slug>/', views.detailTrend,name='detailsTrend'),
    #path('female/<str:slug>/', views.female,name='female'),
    #path('details/<str:slug>/comment/', views.add_comment, name='add_comment'),
    path('details/comments/', include('fluent_comments.urls'))

]
