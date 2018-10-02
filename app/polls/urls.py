from django.urls import path

from . import views

urlpatterns = [
    # /polls/       -> config/urls.py에 polls/로 왔을 때 polls/urls.py에서 처리한다고 되어있기 때문
    path('', views.index, name='index')
]