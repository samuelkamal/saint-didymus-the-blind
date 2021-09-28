from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class SignUp_Form(UserCreationForm):
    username = forms.CharField(max_length=30, label='اسم المستخدم')
    email = forms.EmailField(label='البريد الالكترونى')
    password1 = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='كلمة المرور')
    password2 = forms.CharField(min_length=8, widget=forms.PasswordInput(), label='تأكيد كلمة المرور')
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


System = [
    ("دبلومة العلوم اللاهوتية", "دبلومة العلوم اللاهوتية"),
    ("بكالوريوس العلوم اللاهوتية", "بكالوريوس العلوم اللاهوتية"),
    ("كورسات متخصصة", "كورسات متخصصة"),
    ("دراسات عليا", "دراسات عليا"),
]

class profileform(forms.ModelForm):
    city = forms.CharField(label='المدينة')
    diocese = forms.CharField(label='الإيبارشية')
    church = forms.CharField(label='الكنيسة')
    father_of_confession = forms.CharField(label='اب الاعتراف')
    age = forms.IntegerField(label='السن')
    phone = forms.IntegerField(label='رقم الهاتف')
    qualification = forms.CharField(label='المؤهل')
    job = forms.CharField(label='الوظيفة', help_text='اذا لم تكن هناك وظيفة حاليا اترك الخانة فارغة')
    system = forms.ChoiceField(label='نظام التعليم', choices=System)
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']


class SignIn_Form(forms.ModelForm):
    username = forms.CharField(label='اسم المستخدم')
    password = forms.CharField(widget=forms.PasswordInput(), label='كلمة المرور')
    class Meta:
        model = User
        fields = ['username', 'password']
    