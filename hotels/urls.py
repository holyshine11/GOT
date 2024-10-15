# hotels/urls.py

from django.urls import path
from .views import (
    HotelListView,
    HotelDetailView,
    HotelCreateView,
    HotelUpdateView,
    HotelDeleteView,
)

urlpatterns = [
    path('', HotelListView.as_view(), name='hotel_list'),
    path('create/', HotelCreateView.as_view(), name='hotel_create'),
    path('<int:pk>/', HotelDetailView.as_view(), name='hotel_detail'),
    path('<int:pk>/update/', HotelUpdateView.as_view(), name='hotel_update'),
    path('<int:pk>/delete/', HotelDeleteView.as_view(), name='hotel_delete'),
]