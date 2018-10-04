from django.urls import path, include

from .views import cbv, fbv as views


app_name = 'polls'
urlpatterns_cbv = [
    path('', cbv.IndexView.as_view(), name='index'),
    path('<int:question_id>/', cbv.DetailView.as_view(), name='detail'),
    path('<int:question_id>/results', cbv.ResultsViews.as_view(), name='results'),
    path('<int:question_id>/vote', cbv.VoteView.as_view(), name='vote')
]
urlpatterns = [
    # /polls/       -> config/urls.py에 polls/로 왔을 때 polls/urls.py에서 처리한다고 되어있기 때문
    # name='index'를 통해 네이밍을 해주었기 때문에 config에서 index를 받아온다

    # r'^$'
    path('', views.index, name='index'),
    # r'^(?P<question_id>\d+)/$'
    path('<int:question_id>/', views.detail, name='detail'),
    # r'^(?P<question_id>\d+)/results/$'
    path('<int:question_id>/results/', views.results, name='results'),
    # r'^(?P<question_id>\d+)/vote/$
    path('<int:question_id>/vote/', views.vote, name='vote'),

    # /polls/cbv/로 시작하는 URL요청은
    # 위의 urlpatterns_dbv리스트 내의 내용에서 처리
    path('cbv/', include(urlpatterns_cbv))
]
