from django.forms import ModelForm, BooleanField, TextInput
from django import forms


from .models import Post



class PostForm(ModelForm):
    #post_text = forms.CharField(label='', widget=forms.Textarea(attrs={'class': 'form-control mb-2'})) #добавляет большое поле для ввода текста
    check_box = BooleanField(label='подтвердить') # добавляем галочку, или же true-false поле

    class Meta:
        model = Post
        fields = [ 'author', 'post_type', 'post_title', 'post_text', 'check_box']
        # не забываем включить галочку в поля иначе она не будет показываться на странице!

