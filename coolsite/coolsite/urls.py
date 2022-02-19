"""coolsite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.contrib import admin

from coolsite import settings
from women.views import *
from django.urls import path, include

# import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('captcha/', include('captcha.urls')),
    path('', include('women.urls')),
    # path('__debug__/', include(debug_toolbar.urls)),


    # path('women/', index),
    # path('', index),
    # path('categories/', categories),

]

if settings.DEBUG: # т.е. в режиме отладки к существующим маршрутам добавляются эти с файлами и мультимедиа файлами - НА реальных серверах это и без этого работает
    import debug_toolbar

    urlpatterns = [path('__debug__/', include(debug_toolbar.urls)),] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


handler404 = pageNotFound