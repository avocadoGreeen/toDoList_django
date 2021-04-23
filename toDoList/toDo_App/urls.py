from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create', views.create, name='create'),
    path('<int:pk>/update', views.Update.as_view(), name='update'),
    path('<int:pk>/delete', views.Delete.as_view(), name='delete'),

]
