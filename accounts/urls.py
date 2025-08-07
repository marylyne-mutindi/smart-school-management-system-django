from django.urls import path
from .views import CustomLoginView, login_view
urlpatterns = [
    path('login/', CustomLoginView.as_view(), name='login'),
    path('register/', login_view, name='register'),
]

