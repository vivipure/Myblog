from django.urls import path

from . import views


app_name = 'app'
# router
urlpatterns = [
    path('', views.index, name="index"),
    path('posts/<int:pk>/', views.detail, name="detail"),
]