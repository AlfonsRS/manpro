from django.contrib import admin
from django.urls import path, include
from . import views
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('blogs/', include('blogs.urls', namespace='blogs')),
    path('admin/', admin.site.urls),
    path('', views.welcome, name='home'),
    path('kontak/', views.contact, name='contact'),
    path('accounts/', include('accounts.urls', namespace='')),
    path('usermanagement/', views.usermanagement, name='usermanagement'),
    path('notif/', views.notif, name='notif'),
    path('teammanagement/', views.teammanagement, name='teammanagement'),
    path('profile/', views.profile, name='profile'),
    path('welcome/', views.welcome, name='welcome'),
]

urlpatterns += staticfiles_urlpatterns()
