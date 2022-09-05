from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('index/', views.index, name='index'),
    path('userdrinks', views.userdrinks, name='userdrinks'),
    path('accounts/signup', views.signup, name='signup'),
    path('drinks/<int:drink_id>', views.drinks_detail, name='detail'),
]
