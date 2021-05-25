from django.urls import path
from . import views
urlpatterns = [
       path('',views.learn_var),
       path('w3schools/',views.url1),
]