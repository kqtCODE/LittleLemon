from django.urls import path
from . import views
from djoser.views import TokenCreateView

app_name = 'restaurant'

urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('bookings/', views.BookingListView.as_view({'get': 'list'}), name="bookings"),
    path('menu/', views.menu, name="menu"),
    path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"), 
]