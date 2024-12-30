from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import UserForm
from django.template import loader
from .forms import CustomUserForm
from .models import CustomUser
from django.contrib.auth.decorators import login_required
import hmac
import hashlib
import random
import logging
# Create your views here.

def register(request):
    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = CustomUserForm()
    return render(request,'register.html',{'form':form})


def login_page(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email = email, password = password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            logging.warning('Invalid login attempt')
            return render(request, 'login.html', {'error': 'invalid email or password'})
    return render(request, 'login.html')

@login_required
def get_account_summary(request):
    user = request.user
    if not hasattr(user, 'account_number'):
        user.account_number = str(random.randint(1000000000, 9999999999))
        user.save()
    account_details = CustomUser.objects.get(username=user.username)

    # generating random account number for my bank
    account_number = user.account_number
    secret_key = '321'
    signature = hmac.new(secret_key.encode(),account_number.encode(), hashlib.sha256).hexdigest()   

    context = {
        'account_details': account_details,
        'account_number': account_number,
        'signature': signature,
    }
    return render(request, 'home.html', context)
