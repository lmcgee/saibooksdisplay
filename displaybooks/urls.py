from django.urls import path
from . import views

app_name = 'displaybooks'
urlpatterns = [

    path('', views.home_page, name='home'),
    path('book_list/', views.book_list, name='list'),
    path('home_page/', views.home_page, name='home'),
    path('index1/', views.index1, name='image'),
    path('index2/', views.index2, name='discussion'),
    path('discussion/', views.create_discussion, name='discussion'),
    path('discussion_list/', views.discussion_list, name='discussions'),

]
