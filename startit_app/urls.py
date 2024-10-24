from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('login/', views.login_page, name='login_page'),
    path('quests/detail/<int:pk>/', views.book_page, name='book_page'), 
    path('sign-up/', views.sign_up_page, name='sign_up_page'),
    path('logout/', views.logout_action, name='logout_action'),
    path('quests/<str:filter_type>/<str:filter_value>/', views.filtered_quests, name='filtered_quests'),

]
