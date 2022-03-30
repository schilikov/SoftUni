from django.urls import path

from petstagram.main_app.views.generic import home_view, dashboard_view
from petstagram.main_app.views.pet_photos import pet_photo_details_view, create_pet_photo, edit_pet_photo, \
    like_pet_photo
from petstagram.main_app.views.pets import create_pet, edit_pet, delete_pet
from petstagram.main_app.views.profiles import profile_details_view, create_profile, edit_profile, delete_profile

urlpatterns = (
    path('', home_view, name='home'),
    path('dashboard/', dashboard_view, name='dashboard'),

    path('profile/', profile_details_view, name='profile details'),
    path('profile/create/', create_profile, name='create profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),

    path('photo/details/<int:pk>/', pet_photo_details_view, name='pet photo details'),
    path('photo/add/', create_pet_photo, name='create pet photo'),
    path('photo/edit/<int:pk>/', edit_pet_photo, name='edit pet photo'),
    path('photo/like/<int:pk>/', like_pet_photo, name='like pet photo'),

    path('pet/add/', create_pet, name='create pet'),
    path('pet/edit/<int:pk>/', edit_pet, name='edit pet'),
    path('pet/delete/<int:pk>/', delete_pet, name='delete pet'),
)