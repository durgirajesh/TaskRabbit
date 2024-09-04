from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import login
from .models import UserTasks

class RegisterView(APIView) :
    permission_classes = [AllowAny]
    def post(self, request) :
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not first_name or not last_name or not username or not email or not password :
            return Response({"Invalid User details"})
    
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=password, username=username)
        new_user.save()
        return Response({"User Registration Successfull"})
    
class LoginView(APIView) :
    permission_classes = [AllowAny]
    def post(self, request) :
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password :
            return Response({"username or password cann't be empty"})
        
        user = User.objects.filter(username=username).first()
        if user :
            login(request, user)
            return Response({"Login Successfull"})
    
        return Response({"Invalid User Details"})

class TasksView(APIView) :
    def post(self, request) :
        task_title = request.data.get('title')
        task_description = request.data.get('description')
        username = request.data.get('username')

        if not username or not task_title or not task_description :
            return Response({"Details cann't be empty"})
    
        user = User.objects.filter(username=username).first()
        if not user :
            return Response({"No user found"})
        
        new_task = UserTasks(user=user, task_name=task_title, task_description=task_description)
        new_task.save()
        return Response({f"New Task is create for {username}"})

    def get(self, request) :
        username = request.GET.get('username')

        if not username :
            return Response({"username cann't be empty"})
    
        user = User.objects.filter(username=username).first()
        if not user :
            return Response({"No User found"})
    
        tasks = UserTasks.objects.filter(user=user)
        response = []
        for task in tasks :
            response.append(
                {
                    "title" : task.task_name, 
                    "description" : task.task_description
                }
            )
        
        return Response(response)