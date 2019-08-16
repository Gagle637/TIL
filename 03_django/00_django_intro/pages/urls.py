from django.urls import path
from . import views

urlpatterns = [
    #원래는 app url은 아래로 작성해 나간다.
    path('static_example/', views.static_example),
    path('user_create/', views.user_create),
    path('user_new/', views.user_new),
    path('result/', views.result),
    path('art/', views.art),
    path('catch/', views.catch),
    path('throw/', views.throw),
    path('isitgwangbok/', views.isitgwangbok),
    path('template_language/', views.template_language),
    path('area/<int:r>/', views.area),
    path('time/<int:num1>/<int:num2>/', views.time),
    path('hello/<str:name>/', views.hello),  #str 은 기본값
    path('image/', views.image),
    path('dinner/', views.dinner),
    path('index/', views.index), #url 경로 마지막에 /를 붙이는 습관
    path('introduce/<name>/<int:age>/', views.introduce),
]
