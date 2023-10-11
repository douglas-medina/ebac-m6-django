from django.urls import path

from blog import views


urlpatterns = [
    path('', views.PostView.ss_view(), name='home')
]