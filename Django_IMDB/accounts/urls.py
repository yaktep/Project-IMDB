from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup_view, name='signup'),
    path('login1/', views.login_view1, name='login1'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name="logout")
]