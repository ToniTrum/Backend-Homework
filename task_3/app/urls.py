from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('contents/', views.contents),
    path('contents/<int:content_id>', views.contents)
]