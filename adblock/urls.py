from django.urls import path
from adblock import views


urlpatterns = [
    path('', views.index, name='adblock'),
    path('block/', views.block, name='block'),

]