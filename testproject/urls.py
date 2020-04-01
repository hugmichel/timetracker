"""testproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib.auth import views as auth_views

from timetracker import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='timetracker/login.html')),
    path('logout/', auth_views.LogoutView.as_view(template_name='timetracker/logout.html')),
    path('', views.IndexView.as_view(), name='index'),
    path('add/', views.TimeEntryCreateView.as_view(), name='add'),
    path('remove/<int:time_entry_id>', views.remove_time_entry, name='remove'),
    path('edit/<int:time_entry_id>', views.TimeEntryUpdateView.as_view(), name='edit'),
]
