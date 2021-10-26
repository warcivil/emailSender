from django.urls import path

from app.application.views import EmailInfoView, StatisticsView, EmailView
urlpatterns = [
    path('email/', EmailView.as_view()),
    path('email/<pk>', EmailInfoView.as_view()),
    path('statistics/', StatisticsView.as_view())
]
