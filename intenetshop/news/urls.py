from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.news_home, name='news_home'),
    path('create', views.create, name='create'),
    path('<slug:slug>', views.NewsDetailView.as_view(), name='detail_view'),
    path('<slug:slug>/update', views.NewsUpdateView.as_view(), name='update_view'),
    path('<slug:slug>/delete', views.NewsDeleteView.as_view(), name='delete_view'),
]

