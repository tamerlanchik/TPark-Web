"""ask_kochnov URL Configuration

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
from django.contrib import admin
from django.urls import path
from questions.views import print_params, dynamic
from django.conf.urls.static import static
from django.conf import settings as S

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', print_params),
    path('test_dynamic/', dynamic),
] + static(S.STATIC_URL, document_root=S.STATIC_ROOT)
 
