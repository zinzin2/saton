from django.contrib import admin
from django.urls import path, include
from app import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[
    path('admin/',admin.site.urls),
    path('app/',include('app.urls')),
    path('', views.main, name="main"),
    path('login_app/',include('login_app.urls')),
    # path('career/',include('careers.urlsv'))
]
    