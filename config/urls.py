"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf import settings    #この一文を追加　1ヵ所目
from django.contrib import admin
from django.urls import path, include   #「, include」を追加　2ヵ所目
from django.conf.urls.static import static  #この一文を追加　3ヵ所目

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), #この一文を追加　4ヵ所目
]

if settings.DEBUG:  #この一文を追加　5ヵ所目
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    #この一文を追加　6ヵ所目