from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

@csrf_protect
def logout_view(request):
    if request.method == "POST":
        logout(request)
        return redirect("login")

@csrf_protect
def home_view(request):
    return render(request, 'index.html')

@csrf_protect
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('prompt')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

@csrf_protect
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('prompt')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
@csrf_protect
def prompt_view(request):
    result = None
    if request.method == 'POST':
        text = request.POST.get('prompt_text', '')
        action = request.POST.get('action')
        if action == 'generate':
            result = f"출력 결과: {text}"
        elif action == 'summarize':
            result = f"과정 요약: '{text}'에 기반해 처리되었습니다."
    return render(request, 'prompt.html', {'result': result})
