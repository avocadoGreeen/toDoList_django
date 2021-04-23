from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', include('toDo_App.urls')),
    path('', include('toDo_App.urls')),

]
