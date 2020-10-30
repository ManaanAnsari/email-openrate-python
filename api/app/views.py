from django.shortcuts import render
from django.http import HttpResponse , JsonResponse
from app.models import ImageHash
import random, string
from PIL import Image


# Create your views here.
def load_image(request,i_hash):
    print("\n Loading Image\n"+i_hash)
    red = Image.new('RGB', (1, 1))
    response = HttpResponse(content_type="image/png")
    red.save(response, "PNG")
    if ImageHash.objects.filter(i_hash=i_hash).exists():
        hash_obj = ImageHash.objects.get(i_hash=i_hash)
        hash_obj.status = True
        hash_obj.save()
    return response



def get_image_hash(request):
    response_data = {}
    hash_obj = ImageHash(i_hash=create_hash())
    hash_obj.save()
    response_data["i_hash"] = hash_obj.i_hash
    return JsonResponse(response_data,status=200)    

def get_hash_status(request,i_hash):
    response_data = {}
    if ImageHash.objects.filter(i_hash=i_hash).exists():
        hash_obj = ImageHash.objects.get(i_hash=i_hash)
        response_data["i_hash"] = hash_obj.i_hash
        response_data["status"] = hash_obj.status
        return JsonResponse(response_data,status=200)
    response_data["message"] = "hash not found"
    return JsonResponse(response_data,status=406)


def create_hash():
    hash_text = "".join(random.choices(string.ascii_lowercase + string.digits, k=64))
    while ImageHash.objects.filter(i_hash=hash_text).exists():
        hash_text = "".join(random.choices(string.ascii_lowercase + string.digits, k=64))
    return hash_text
