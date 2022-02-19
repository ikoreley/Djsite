from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, FormView

from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import *
from .models import *
from .utils import *
# Create your views here.

# menu = ["О сайте", "Добавить статью", "Обратная связь", "Войти"]

#->убрали в 11уроке в домашке
#->и перенесли на 17уроке в файл utils.py
# menu = [{'title': 'О сайте', 'url_name': 'about'},
#         {'title': 'Добавить статью', 'url_name': 'add_page'},
#         {'title': 'Обратная связь','url_name': 'contact'},
#         {'title': 'Войти','url_name': 'login'},
# ]


#класс представления
class WomenHome(DataMixin, ListView): # этот класс будет отвечать за главную страницу сайта
    paginate_by = 3
    model = Women # атрибут ссылается на модель Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    # extra_context = {'title': 'Главная страница'}

    def get_context_data(self, *, object_list=None, **kwargs):
        # обращаемся к базовому классу и берем существующий контекст
        context = super().get_context_data(**kwargs) # **kwargs - передаем все именованные параметры
        # # context['menu'] = menu # я запилил меню в шаблон "list_menu.html" давно
        # context['title'] = 'Главная страница'
        # context['cat_selected'] = 0 # делает нажатой "Все категории" на главной странице
        c_def = self.get_user_context(title='Главная страница')

        # объединяем словари в один
        return dict(list(context.items()) + list(c_def.items()))


    # в этой функции выбираем то что будем отображать из модели , функция формирует список
    def get_queryset(self):
        return Women.objects.filter(is_published=True).select_related('cat') # возвращаем модели только отмеченные к публикации

# # прописываем представление нашей главной страницы через функцию
# def index(request): # HttpRequest (index - проссто имя и может быть любым)
#     # return HttpResponse("Страница приложения women.") # заменим страницу на шаблон
#     posts = Women.objects.all()
#     # cats = Category.objects.all() #->убрали в 11уроке
#
#     paramm = {
#         'posts': posts,
#         # 'cats': cats, #->убрали в 11уроке
#         # 'menu': menu, #->убрали в 11уроке в домашке
#         'title': 'Главная страница',
#         'cat_selected': 0,
#     }
#
#     return render(request, 'women/index.html', context=paramm)

# @login_required
def about(request): # HttpRequest (index - проссто имя и может быть любым)
    contact_list =Women.objects.all()      # сохраняем список объектов модели в переменную

    #пример пагинации в 18 уроке
    # paginator = Paginator(contact_list, 3) # создаем экземпляр класса Paginator указывая список и кол-во элементов на странице
    # page_number = request.GET.get('page')  # получаем номер страницы с GET запроса
    # page_obj = paginator.get_page(page_number)  # фармируем список элементов текущей страницы
    # return render(request, 'women/about.html', {'page_obj': page_obj, 'menu':menu, 'title': 'О сайте' }) # 'menu':menu,

    return render(request, 'women/about.html', {'menu':menu, 'title': 'О сайте' }) # 'menu':menu,
    # return HttpResponse("Страница п:*риложения women.") # заменим страницу на шаблон


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    form_class = AddPostForm
    template_name = 'women/add_page.html'
    # success_url = reverse_lazy('home_redirect') #адрес куда добавлять новую статью если в нашей модели не прописан метод "def get_absolute_url"
    # reverse_lazy - создает маршрут в момент когда он понадобится, а reverse - создает маршрут сразу НО если его еще нет будет ошибка
    login_url = reverse_lazy('login') #'/admin'
    raise_exception = True  # отображает страницу "403 Forbidden" Доступ запрещен если не зарегистрирован

    def get_context_data(self, *, object_list=None, **kwargs):
        # обращаемся к базовому классу и берем существующий контекст
        context = super().get_context_data(**kwargs) # **kwargs - передаем все именованные параметры
        # # context['menu'] = menu # я запилил меню в шаблон "list_categories.html" давно
        # context['title'] = 'Добавление статьи'
        c_def = self.get_user_context(title='Добавление статьи')
        return dict(list(context.items()) + list(c_def.items()))





# def add_page(request): #
#     # return HttpResponse("Добавление статьи")
#     if request.method == 'POST':          # если пользователь нажал отправить(т.е. сработал метод POST)
#         form = AddPostForm(request.POST, request.FILES)  # формируется форма на основе объекта словаря POST где хранятся заполненые данные
#         if form.is_valid():               # если данные не прошли проверку то форма вернется с заполнеными полями
#             # print(form.cleaned_data)      # если данные прошли проверку, то отобразим в консоли очищенные данные
#             # try:
#             #     # Women.objects.create(**form.cleaned_data) # для НЕСВЯЗАННОЙ ФОРМЫ
#             #     form.save()   # встроенная в форме сохраняет в базу данных модели 'Women'
#             #     return redirect('home_redirect')
#             # except:
#             #     form.add_error(None, "Ошибка добавления поста")
#             form.save()  # встроенная в форме сохраняет в базу данных модели 'Women' тут уже есть встроенная генерация ошибок
#             return redirect('home_redirect')
#
#     else:
#         form = AddPostForm()
#
#     return render(request, 'women/add_page.html', {'form': form, 'title': "Добавление статьи",}) # 'menu': menu,


#### в место функции пропишем класс представления "class ContactFormView(DataMixin, FormView):"
# def contact(request): #
#     # return HttpResponse("Обратная связь")
#     return render(request, 'women/contact.html', {'title': "Обратная связь", })  # 'menu': menu,

class ContactFormView(DataMixin, FormView):
    form_class = ContactForm
    template_name = 'women/contact.html'
    success_url = reverse_lazy('home_redirect')

    # метод формирует контекст для шаблона
    def get_context_data(self, *, object_list=None, **kwargs):
        # обращаемся к базовому классу и берем существующий контекст
        context = super().get_context_data(**kwargs) # **kwargs - передаем все именованные параметры
        c_def = self.get_user_context(title="Обратная связь")
        return dict(list(context.items()) + list(c_def.items()))

    # метод вызывается когда пользователь заполнил все верно
    def form_valid(self, form):
        print(form.cleaned_data)
        return redirect('home_redirect')


# Закоментировали в уроке 20
# def login(request): #
#     return HttpResponse("Авторизация")


# def show_post(request, post_slug): #
#     post = get_object_or_404(Women, slug=post_slug)
#
#     context = {
#         'post': post,
#         # 'menu': menu,
#         'title': post.title,
#         # 'cat_selected': post.cat_id, # эта строка при выборе "читать пост" выбирает категорию выбранной статьи и делает ее нажатой неактивной
#     }
#     # return HttpResponse(f"Отображение статьи с id = {post_id}")
#     return render(request, 'women/post.html', context=context)

class ShowPost(DataMixin, DetailView):
    model = Women
    template_name = 'women/post.html'
    slug_url_kwarg = 'post_slug' # pk_url_kwarg = '****' -если используем "pk"
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        # обращаемся к базовому классу и берем существующий контекст
        context = super().get_context_data(**kwargs) # **kwargs - передаем все именованные параметры
        # context['menu'] = menu # я запилил меню в шаблон "list_categories.html" давно
        # context['title'] = context['post']
        # return context
        c_def = self.get_user_context(title=context['post'])
        return dict(list(context.items()) + list(c_def.items()))


class WomenCategory(DataMixin, ListView):
    model = Women
    template_name = 'women/index.html'
    context_object_name = 'posts'
    allow_empty = False # выдает страницу "404" когда нет статей

    # в этой функции выбираем то что будем отображать из модели , функция формирует список
    def get_queryset(self):
        return Women.objects.filter(cat__slug=self.kwargs['cat_slug'],is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        # обращаемся к базовому классу и берем существующий контекст
        context = super().get_context_data(**kwargs) # **kwargs - передаем все именованные параметры
        # # context['menu'] = menu # я запилил меню в шаблон "list_categories.html" давно
        # context['title'] = 'Категория - '+str(context['posts'][0].cat)
        # context['cat_selected'] = context['posts'][0].cat_id # делает нажатой "Все категории" на главной странице
        # return context
        # c_def = self.get_user_context(title='Категория - '+str(context['posts'][0].cat),
        #                               cat_selected=context['posts'][0].cat_id)
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - '+str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))

# def show_category(request, cat_slug): #
#     # return HttpResponse(f"Отображение категории с id = {cat_id}")
#     cat = Category.objects.filter(slug=cat_slug)
#     posts = Women.objects.filter(cat_id=cat[0].id)
#     # cats = Category.objects.all() #->убрали в 11уроке
#
#
#     if len(posts) == 0: #
#         raise Http404()
#
#     paramm = {
#         'posts': posts,
#         # 'cats': cats, #->убрали в 11уроке
#         # 'menu': menu, #->убрали в 11уроке в домашке
#         'title': 'Отображение по рубрикам',
#         'cat_selected': cat[0].id,
#     }
#     return render(request, 'women/index.html', context=paramm)



# def categories(request, catid): # HttpRequest (index - проссто имя и может быть любым)
#     if request.GET: # если будет get запрос пример: ?name=Gagarina&type=pop
#         print(request.GET) # урок 03
#     if request.POST:  #
#         print(request.POST)  # урок 03
#     return HttpResponse(f"<h1>Статьи по категориям</h1><p>{catid}</p>")
#
# def archive(request, year): #
#     if int(year) > 2021:
#         return redirect('home', permanent=False) # 302 - временный редирект
#
#         # return redirect('/', permanent=True) # 301 - постоянный редирект
#         # return redirect('/', permanent=False) # 302 - временный редирект
#         # return redirect('/') # 302 - временный редирект
#         # raise Http404() # когда генерируется исключение оно попадает в pageNotFound в атрибут exception
#
#     return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")

def pageNotFound(requests, exception):
    return HttpResponseNotFound('<h1>упссс Страница не найдена</h1>')

class RegisterUser(DataMixin, CreateView):
    # form_class = UserCreationForm  # берем стандартную форму регистрации Django
    form_class = RegisterUserForm  # берем свою созданную форму
    template_name = 'women/register.html' # ссылка на шаблон страницы
    success_url = reverse_lazy('login')   # перенаправление на страницу при успешной регистрации

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs) # **kwargs - передаем все именованные параметры
        c_def = self.get_user_context(title='Регистрация')
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form): # метод вызывается при успешной регистрации
        user = form.save() # сохраняем форму в базу данных-добавляем пользователя в базу данных
        login(self.request, user) # авторизовываем пользователя
        return redirect('home_redirect') # перенаправляем на главную страницу


class LoginUser(DataMixin, LoginView):  # стандартный класс представления
    # form_class = AuthenticationForm  # стандартная форма авторизации
    form_class = LoginUserForm  # НАША созданная форма авторизации
    template_name = 'women/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация")
        return  dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('home_redirect')

def logout_user(request):
    logout(request)
    return redirect('login')


