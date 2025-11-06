from django.urls import path
from .import views
urlpatterns = [
    path('',views.Display),
    path('sumbit',views.Details,name='details'),
]
