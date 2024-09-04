from django.urls import path
from .views import RegisterView, LoginView, TasksView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'), 
    path('login/', LoginView.as_view(), name='login'), 
    path('task/', TasksView.as_view(), name='tasks')
]
