from django.contrib import admin
from django.urls import path
from demoapp import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('', views.send_mail_page)
]