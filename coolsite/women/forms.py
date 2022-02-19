from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField

from .models import *

# класс формы - НЕСВЯЗАННАЯ ФОРМА
# class AddPostForm(forms.Form): # класс для нашей формы
#     # прописываем только те поля которые будем отображать пользователю (такие поля как 'time_create' и 'time_update' создадутся автоматически)
#     title = forms.CharField(max_length=255, label="Заголовок", widget=forms.TimeInput(attrs={'class': 'form-input'})) # класс "CharField" для поля ввода данных
#     slug = forms.SlugField(max_length=255, label="URL")  # класс "SlugField"
#     content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'row': 10}), label='Контент')
#     is_published = forms.BooleanField(label='Публикация', required=False, initial=True) # класс "BooleanField" для установки чекбокса, для установки флага "публиковать статью или нет"
#     cat = forms.ModelChoiceField(queryset=Category.objects.all(), label="Категории", empty_label="Категория не выбрана") # "ModelChoiceField" создает выпадающий список для выбора категории


# класс формы - СВЯЗАННАЯ ФОРМА
class AddPostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"

    class Meta:
        model = Women       # делает сыязь формы с моделью
        # fields = '__all__'  # какие поля нужно отобразить в форме
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']
        widget = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'row': 10}),
        }

    #  clean_ + поле которое хотим валидировать
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 100:
            raise ValidationError('Длина превышает 100 символов')
        return title

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class':'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:    # расширяем класс UserCreationForm
        model = User  # User с нашей базы данных "auth_user"
        fields = ('username', 'email', 'password1', 'password2') # указываем поля которые мы будем отображать

        # оформление для каждого поля, имена берем из кода элементов страницы с помощью браузера
        # widgets = {
        #     'username': forms.TextInput(attrs={'class':'form-input'}),
        #     'password1': forms.PasswordInput(attrs={'class': 'form-input'}),
        #     'password2': forms.PasswordInput(attrs={'class': 'form-input'}),
        # }


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))


class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    capatcha = CaptchaField()



