from django.db import models

# Create your models here.
from django.urls import reverse


class Women(models.Model):
    # id - это поле прописывается автоматом в базах данных
    title = models.CharField(max_length=255, verbose_name="Заголовок")
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True, verbose_name="Текст статьи")
    photo = models.ImageField(upload_to="photos/%Y/%m/%d/", verbose_name="Фото") # шаблон папок "photos/%Y/%m/%d/" для хранения загруженных фото

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Время создания") # дата создания
    time_update = models.DateTimeField(auto_now=True, verbose_name="Время изменения")     # дата обновленя
    is_published = models.BooleanField(default=True, verbose_name="Публикация")
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Категория") #
    # автоматом появляется индитификатор cat_id и мы можем его использовать
                    #'Category' прописываем строкой потомучто class Category еще не определен он находится ниже

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # return reverse('post', kwargs={'post_id': self.pk})
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины' # убирает автоматическую подстановку 's' Джанго множественного названия
        # ordering = [ 'title',] # порядок сортировки (инверсия знаком '-')

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория') # db_index - это означает что поле будет индексированно и поиск будет быстрее
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name="URL")


    def __str__(self):
        return self.name


    def get_absolute_url(self):
        # return reverse('category', kwargs={'cat_id': self.cat_id})
        return reverse('category', kwargs={'cat_slug': self.slug})


    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'
        ordering = ['id']

