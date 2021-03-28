from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('index',views.index),
    path('register/',views.registerPage, name ="register"),
    path('login/', views.loginPage, name = "login"),
    path('introcs/',views.registerPage, name ="introcs"),
    path('expos/',views.registerPage, name ="expos"),
    path('DS/',views.registerPage, name ="DS"),
    path('physics/',views.registerPage, name ="physics"),
    path('chemistry/',views.registerPage, name ="chemistry"),
    path('musictheory/',views.registerPage, name ="musictheory"),
]