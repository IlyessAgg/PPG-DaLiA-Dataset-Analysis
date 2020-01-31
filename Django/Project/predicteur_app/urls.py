from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('predict/', views.predict, name='to_predict')
]