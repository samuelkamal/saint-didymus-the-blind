from django.contrib.auth.decorators import login_required
from Accounts.models import Profile
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from .forms import SignUp_Form, profileform, SignIn_Form
from MainPage.models import Dibloma, Bachelor, Specialized_Courses, Postgraduate
from django.contrib import messages
# Create your views here.


def signup(request):
    if 'signup' in request.POST and request.method=='POST':
        form = SignUp_Form(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('profile')

    else:
        form = SignUp_Form()

    if 'login' in request.POST and request.method=='POST':
        logform = SignIn_Form()
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f'مرحبا بك, {username}')
            return redirect('courses')
        else:
            messages.warning(request, 'كلمة المرور او اسم المستخدم غير صحيحة.')

    else:
        logform = SignIn_Form()

    return render(request, 'accounts/signup.html', context={
        'form' : form,
        'logform' : logform
    })

def more_info(request):
    profile = Profile.objects.get(user=request.user)
    if request.method=='POST':
        profile_F = profileform(request.POST, instance=profile)
        if profile_F.is_valid():
            userprofile = profile_F.save(commit=False)
            userprofile.user = request.user
            userprofile.save()
            messages.success(request, f'مرحبا بك, {userprofile.user}')
            return redirect('courses')

    else:
        profile_F = profileform()

    return render(request, 'accounts/profile.html', context={
        'profile' : profile_F
    })

@login_required
def courses(request):
    return render(request, 'accounts/courses.html', context={
        'dip' : Dibloma.objects.all(),
        'bach' : Bachelor.objects.all(),
        'spe_cour' : Specialized_Courses.objects.all(),
        'post' : Postgraduate.objects.all()
    })

def Logout(request):
    logout(request)
    return render(request, 'accounts/logout.html')