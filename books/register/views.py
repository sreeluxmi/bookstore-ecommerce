from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

# from django.views import generic
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy


# Create your views here.


def signup(request):
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(username=request.POST['username'])
                return render(request, 'signup.html', {'error': 'Username is already taken!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return redirect('login')
        else:
            return render(request, 'signup.html', {'error': 'Password does not match!'})
    else:
        return render(request, 'signup.html')


# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(username=request.POST['username'], password=request.POST['password'])
        if user is not None:
            auth.login(request, user)
            return redirect('list')
        else:
            return render(request, 'login.html', {'error': 'Username or password is incorrect!'})
    else:
        return render(request, 'login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
    return redirect('signup')
