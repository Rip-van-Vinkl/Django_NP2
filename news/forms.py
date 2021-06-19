from django.forms import ModelForm, BooleanField, TextInput
from django import forms

from .models import Post


from django.contrib.auth.forms import UserCreationForm


from allauth.account.forms import SignupForm
from django.contrib.auth.models import User, Group


class PostForm(ModelForm):
    #post_text = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control mb-2'})) #добавляет большое поле для ввода текста
    check_box = BooleanField(label='подтвердить') # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = [ 'author', 'post_type', 'post_title', 'post_text', 'check_box']
        # не забываем включить галочку в поля иначе она не будет показываться на странице!



class UserForm(ModelForm):
    username = forms.CharField(label='Логин')
    first_name = forms.CharField(label='Имя')
    last_name = forms.CharField(label='Фамилия')
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


class BasicSignupForm(SignupForm):

    def save(self, request):
        user = super(BasicSignupForm, self).save(request)
        basic_group = Group.objects.get(name='common')
        basic_group.user_set.add(user)
        return user


class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label = "Email")
    first_name = forms.CharField(label = "Имя")
    last_name = forms.CharField(label = "Фамилия")

    class Meta:
        model = User
        fields = ("username", 
                  "first_name", 
                  "last_name", 
                  "email", 
                  "password1", 
                  "password2", )