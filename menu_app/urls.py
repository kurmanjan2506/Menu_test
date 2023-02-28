from django.urls import path
from .views import base, index, get_id


urlpatterns = [
    path('', base, name='category'),
    path('dish/', index, name='dish'),
    path('dish/<int:pk>/', get_id, name='dish-detail'),
]