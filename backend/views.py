from backend.settings import BASE_DIR
from django.shortcuts import render
from . forms import ImageForm
from .compression import compress
import os

def image_upload_view(request):
    """Process images uploaded by users"""
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            # Get the current instance object to display in the template
            img_obj = form.instance
            print("Compressing", BASE_DIR, img_obj.image.url)
            compress(str(BASE_DIR) + img_obj.image.url)

            return render(request, 'index.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()

    return render(request, 'index.html', {'form': form})
