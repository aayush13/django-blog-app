from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name="blog-home"), # name helps in reverse lookup - multiple apps with same route
    path('about/', views.about, name="blog-about"),
]