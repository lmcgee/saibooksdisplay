"""saibookdisplay URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:

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
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

from displaybooks import views

app_name = 'displaybooks'
urlpatterns = [
               #path('displaybooks/', include('displaybooks.urls', namespace='displaybooks')),
    path('', views.home_page),
    path('displaybooks/', include('displaybooks.urls', namespace='displaybooks')),
    path('discussion/', views.create_discussion, name='discussion'),
               #path('hero-slider/', include('hero_slider.urls')),
    path('admin/', admin.site.urls),
    path('comments/', include('django_comments.urls')),
    path('', RedirectView.as_view(url='/displaybooks/')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#Add Django site authentication urls (for login, logout, password management)
urlpatterns += [
                path('accounts/', include('django.contrib.auth.urls')),
                ]
