from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView, Response, status


class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'registration/profile.html'


class LoginView(APIView):
    def post(self, request):
        user = authenticate(
            request,
            username=request.data.get('username'),
            password=request.data.get('password')
        )
        if user is None:
            return Response({'detail': 'Incorrect username or password'}, status.HTTP_401_UNAUTHORIZED)
        else:
            login(request, user)
            return Response(None, status.HTTP_204_NO_CONTENT)


class LogoutView(APIView):
    def post(self, request):
        if request.user.is_authenticated:
            logout(request)
            return Response(None, status.HTTP_204_NO_CONTENT)
        else:
            return Response({'detail': 'Not logged in'}, status.HTTP_401_UNAUTHORIZED)
