from django.urls import include, path
from django.contrib.auth.views import logout_then_login
from .views import ProfileView

urlpatterns = [
    path('logout/', logout_then_login, name='logout_login'),
    path('logout/?next=<str:login_url>',
         logout_then_login),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('', include('django.contrib.auth.urls')),
]
