from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    # path('index/',views.index, name = "index"),
    path('register/',views.registerPage, name ="register"),
    path('login/', views.loginPage, name = "login"),
    path('introcs/',views.introcsPage, name ="introcs"),
    path('expos/',views.exposPage, name ="expos"),
    path('DS/',views.DSPage, name ="DS"),
    path('physics/',views.physicsPage, name ="physics"),
    path('chemistry/',views.chemistryPage, name ="chemistry"),
    path('musictheory/',views.musictheoryPage, name ="musictheory"),
    path('userHome/',views.userHome, name ="userHome")
]