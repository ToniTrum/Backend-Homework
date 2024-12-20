from django.urls import path
from . import views

urlpatterns = [
    path('', views.main),
    path('contents/', views.get_all_contents),
    path('contents/<int:content_id>', views.get_content),
    path('create/', views.create)
]