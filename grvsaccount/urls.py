from django.urls import include, path
from django.contrib.auth.views import logout_then_login
from . import views

urlpatterns = [
    path('api/login/', views.LoginView.as_view()),
    path('api/logout/', views.LogoutView.as_view()),
    path('logout/', logout_then_login, name='logout_login'),
    path('logout/?next=<str:login_url>',
         logout_then_login),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('apitest/', views.TemplateView.as_view(template_name='grvsaccount/login.html')),
    path('', include('django.contrib.auth.urls')),
]
