from .views import *
from django.urls import path

app_name='freeboard'
urlpatterns=[
    path('', BoardLV.as_view(), name='board'),
    path('<int:pk>/', BoardDV.as_view(), name='board_detail'),
]