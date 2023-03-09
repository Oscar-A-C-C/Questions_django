from django.urls import path

from . import views
app_name = "polls"
urlpatterns = [
    #ex /polls/
    path("", views.IndexView.as_view(), name="index"),
    #ex /polls/#/detail
    path("<int:pk>/", views.DetailView.as_view(), name="detail"),
    #ex /polls/#/results
    path("<int:pk>/results/", views.ResultView.as_view(), name="results"),
    #ex /polls/#/votes
    path("<int:question_id>/votes/", views.votes, name="votes")
]