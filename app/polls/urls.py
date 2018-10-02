from django.urls import path

from . import views


urlpatterns = [
    # /polls/       -> config/urls.py에 polls/로 왔을 때 polls/urls.py에서 처리한다고 되어있기 때문
    # name='index'를 통해 네이밍을 해주었기 때문에 config에서 index를 받아온다
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
