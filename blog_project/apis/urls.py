from django.urls import path
from .views import BlogAPIView

urlpatterns = [
    path("<int:pk>/", BlogApiDetail.as_view(), name="post_detail"),
    path("", BlogAPIView.as_view(), name="blog_list"),
]
