from django.shortcuts import render, redirect

from petstagram.main_app.helpers import get_profile
from petstagram.main_app.models import PetPhoto


def pet_photo_details_view(request, pk):
    pet_photo = PetPhoto.objects\
        .prefetch_related('tagged_pets')\
        .get(pk=pk)

    context = {
        'pet_photo': pet_photo,
    }
    return render(request, 'photo_details.html', context)


def like_pet_photo(request, pk):
    pet_photo = PetPhoto.objects.get(pk=pk)
    pet_photo.likes += 1
    pet_photo.save()

    return redirect('pet photo details', pk)


def create_pet_photo(request):
    return render(request, 'photo_create.html')


def edit_pet_photo(request):
    return render(request, 'photo_edit.html')