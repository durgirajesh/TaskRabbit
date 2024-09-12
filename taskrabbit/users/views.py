from django.contrib.auth.models import User
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from django.contrib.auth import login, authenticate
from .models import UserTasks
from django.contrib.auth.hashers import make_password

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

        hashed_password = make_password(password)
        new_user = User(first_name=first_name, last_name=last_name, email=email, password=hashed_password, username=username)
        new_user.save()
        return Response({"User Registration Successfull"})
    
class LoginView(APIView) :
    permission_classes = [AllowAny]
    def post(self, request) :
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password :
            return Response({"username or password cann't be empty"})
        
        user = authenticate(username=username, password=password)
        if user :
            login(request, user)
            return Response({"Login Successfull"})
    
        return Response({"Invalid User Details"})


class TasksView(APIView) :
    permission_classes = [IsAuthenticated]
    def post(self, request) :
        task_title = request.data.get('title')
        task_description = request.data.get('description')

        if not task_title or not task_description :
            return Response({"Details cann't be empty"})
    
        user = request.user
        new_task = UserTasks(user=user, task_name=task_title, task_description=task_description)
        new_task.save()
        return Response({f"New Task is created for {user.username}"})

    def get(self, request) :
        user = request.user
        if not user :
            return Response({"No User found"})
    
        tasks = UserTasks.objects.filter(user=user)
        response = []
        response.append({"user" : user.username})
        for task in tasks :
            response.append(
                {
                    "title" : task.task_name, 
                    "description" : task.task_description
                }
            )
        
        return Response(response)