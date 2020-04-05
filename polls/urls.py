from django.urls import path

from . import views

app_name = 'polls'
urlpatterns = [
    path('', views.BaseView.as_views(), name='base'),
    path('<int:pk>', views.DetailView.as_views(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_views(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote')
]
