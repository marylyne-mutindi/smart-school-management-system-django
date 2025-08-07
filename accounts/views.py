from django.contrib.auth.views import LoginView
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render
from django.contrib.auth import authenticate, login

class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'  # Update if you rename your login page
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

def login_view(request):
    if request.method == 'POST':
        # Handle login logic here
        pass
    return render(request, 'accounts/login.html')
