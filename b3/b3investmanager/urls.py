from django.urls import path

from . import views

urlpatterns = [
    # indexes
    path("", views.index, name="index"),

    path("code_index/", views.code_index, name="code_index"),

    path("investment_index/", views.investment_index, name="investment_index"),

    # addictions
    path("add_code/", views.add_code, name="add_code"),

    path("add_investment/", views.add_investment, name="add_investment"),

    path('code/<int:pk>/delete/', views.delete_code, name='delete-code'),
    
    path('investment/<int:pk>/delete/', views.delete_investment, name='delete-investment'),

    # ex: /polls/5/
    path("<int:question_id>/", views.detail, name="detail"),
    # ex: /polls/5/results/
    path("<int:question_id>/results/", views.results, name="results"),
    # ex: /polls/5/vote/
    path("<int:question_id>/vote/", views.vote, name="vote"),
]
