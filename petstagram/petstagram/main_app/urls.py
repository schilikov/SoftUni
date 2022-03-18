from django.urls import path

from petstagram.main_app.views import home_view, dashboard_view, profile_details_view, pet_photo_details_view, \
    like_pet_photo

urlpatterns = (
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),
    path('profile/', profile_details_view, name='profile details'),
    path('photo/details/<int:pk>/', pet_photo_details_view, name='pet photo details'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),
)