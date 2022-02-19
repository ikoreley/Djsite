from django.db.models import Count
from django.core.cache import cache

from .models import *

menu = [{'title': 'О сайте', 'url_name': 'about'},
        {'title': 'Добавить статью', 'url_name': 'add_page'},
        {'title': 'Обратная связь','url_name': 'contact'},
        # {'title': 'Войти','url_name': 'login'},
]


class DataMixin:
    paginate_by = 20
    # метод создает контекст для шаблона по умолчанию
    def get_user_context(self, **kwargs):
        context = kwargs               # формируем словарь из переданных параметров
        # cats = Category.objects.all()  # формируем список категорий

        cats = cache.get('cats')
        if not cats:
            cats = Category.objects.annotate(Count('women'))  # формируем список категорий Агрегурующей функцией
            cache.set('cats', cats, 60)

        # для примера как убрать меню для незарегистрированных пользователей
        user_menu = menu.copy()
        if not self.request.user.is_authenticated:
            user_menu .pop(1)

        context['menu'] = user_menu

        context['cats'] = cats
        if 'cat_selected' not in context:
            context['cat_selected'] = 0  # делает нажатой "Все категории" на главной странице
        return context








