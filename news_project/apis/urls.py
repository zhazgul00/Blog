from django.urls import path
from .views import NewsAPIView

urlpatterns = [
    path("<int:pk>/", NewsApiDetail.as_view(), name="news_detail"),
    path("", NewsAPIView.as_view(), name="news_list"),
]
