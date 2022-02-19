from django.urls import path, re_path, include
from django.views.decorators.cache import cache_page

from women.views import *

urlpatterns = [
    # path('', index, name='home_redirect'), # http://127.0.0.1:8000/
    path('', WomenHome.as_view(), name='home_redirect'), # http://127.0.0.1:8000/
    # path('', cache_page(60)(WomenHome.as_view()), name='home_redirect'), # загрузка с кешированием

    path('about/', about, name='about'), #
    # path('add_page/', add_page, name='add_page'), #
    path('add_page/', AddPage.as_view(), name='add_page'), #
    # path('contact/', contact, name='contact'), #
    path('contact/', ContactFormView.as_view(), name='contact'), #
    # path('login/', login, name='login'), #
    path('login/', LoginUser.as_view(), name='login'), #
    path('logout/', logout_user, name='logout'), #
    path('register/', RegisterUser.as_view(), name='register'), #
    # path('post/<slug:post_slug>/', show_post, name='post'), #
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'), #
    # path('category/<slug:cat_slug>/', show_category, name='category'), #
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'), #

    # path('__debug__/', include('debug_toolbar.urls')),

    # path('hi-redirect/', index, name='home_redirect'), # для примера редиректа на страницу
    # path('women/', index),
    # path('categories/<int:cat_id>/', categories),
    # path('categories/<slug:cat_id>/', categories),
    # re_path(r'^archive/(?P<year>[0-9]{4})/', archive),
]
