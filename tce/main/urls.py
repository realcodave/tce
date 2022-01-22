from django.urls import path
from .views import Index, About, LiveStream, Detail, Article

urlpatterns = [
    path("", Index, name="index"),
    path("article/", Article, name="article"),
    path('about/', About.as_view(), name="about"),
    path("livestream/", LiveStream.as_view(), name="live"),
    path("detail/<slug>/", Detail, name="detail"),
]
