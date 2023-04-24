from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),

    path("code_index/", views.code_index, name="code_index"),
    
    path("investment_index/", views.investment_index, name="investment_index"),
    
    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]