from django.urls import path
from schoolNews import views

app_name = 'schoolNews'

urlpatterns = [
    path('', views.index, name='index'),
]