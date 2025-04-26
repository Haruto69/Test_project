from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .forms import CustomUserCreationForm
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt  # <-- ADD THIS
import json

# Traditional Django Views (for server-rendered templates)
def register_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('welcome')
        messages.error(request, 'Registration failed')
    else:
        form = CustomUserCreationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('welcome')
        messages.error(request, 'Invalid credentials')
    return render(request, 'accounts/login.html')

def welcome_view(request):
    if not request.user.is_authenticated:
        return redirect('login')
    return render(request, 'accounts/welcome.html', {'username': request.user.username})

def custom_logout(request):
    logout(request)
    messages.success(request, "Logged out successfully")
    return redirect('login')

# API Endpoints (for Next.js)

@csrf_exempt   # <-- ADD THIS
@api_view(['POST'])
def api_login(request):
    """
    API view to handle login requests from the frontend (Next.js).
    Expects username and password in the request body.
    """
    data = request.data
    username = data.get('username')
    password = data.get('password')

    # Authenticate the user
    user = authenticate(request, username=username, password=password)
    if user:
        login(request, user)
        return JsonResponse({'status': 'success', 'user': user.username})
    return JsonResponse({'status': 'error', 'message': 'Invalid credentials'}, status=401)

@csrf_exempt   # <-- ADD THIS
@api_view(['POST'])
def api_register(request):
    """
    API view to handle user registration requests from the frontend (Next.js).
    Expects username and password in the request body.
    """
    data = request.data
    username = data.get('username')
    password = data.get('password')

    # Create a new user using the CustomUserCreationForm
    form = CustomUserCreationForm(data)
    if form.is_valid():
        user = form.save()
        return JsonResponse({'status': 'success', 'user': user.username})
    return JsonResponse({'status': 'error', 'errors': form.errors}, status=400)

@csrf_exempt   # <-- ADD THIS
@api_view(['POST'])
def api_logout(request):
    """
    API view to handle logout requests from the frontend (Next.js).
    This will clear the session and return a JSON response.
    """
    logout(request)
    return JsonResponse({'status': 'success'}, status=200)
