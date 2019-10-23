from django.urls import path
from . import views


app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),   
    path('delete/', views.delete, name='delete'),   
    path('update/', views.update, name='update'),
    path('password/', views.change_password, name='password'),
    path('<username>/', views.profile, name='profile'), #맨 위에있으면 오류남 모든 url이 문자열인대 이 url은 모든 문자열을 포함하고 있기 때문에
]
