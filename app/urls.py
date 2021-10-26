from app.application.views import EmailView
from django.urls import path

from app.application.views import EmailInfoView

from app.application.views import StatisticsView

urlpatterns = [
    path('email/', EmailView.as_view()),
    path('email/<pk>', EmailInfoView.as_view()),
    path('statistics/', StatisticsView.as_view())
]
