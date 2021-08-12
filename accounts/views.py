from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from jobs.views import createJob
from django.contrib.auth import logout
# Create your views here.
def signup(request):
    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # if password match
        if password == password2:
            if User.objects.filter(username = username).exists():
                messages.error(request, 'That user name already taken')
                return redirect('signup')
            else:
                if User.objects.filter(email = email).exists():
                    messages.error(request, 'That email already taken')
                    return redirect('signup')
                else:
                     user = User.objects.create_user(username = username, password=password, email=email,)
                     #auth.login(request,user)
                     #messages.success(request, 'you are now login')
                     #return redirect('index')
                     user.save()
                     messages.success(request, 'you are now registered and can login')
                     return redirect('login')



        else:
            messages.error(request, 'passwords not match')
            return redirect('signup')
    else:
        return render(request, 'accounts/signup.html')
    
    

    
    
    


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            if user.is_superuser:
                auth.login(request, user)
                messages.success(request, 'you are login')
                return redirect('createJob')
            else:
                auth.login(request, user)
                return redirect('jobList')

        else:
            messages.error(request, 'Invalid unser password')
            return redirect('login')

    else:
        return render(request, 'accounts/login.html')

@login_required(login_url='/login/')
def logout(request):
    
    auth.logout(request)
    return redirect('login')