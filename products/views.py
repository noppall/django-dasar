from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, Http404
from .models import Products

# Create your views here.
def home_view(request, *args, **kwargs):
    context = {"name": "nopal"}
    return render(request, "home.html", context)

def product_detail__view(request, id):
    try:
        obj = Products.objects.get(id=id)
    except:
        raise Http404
    return render(request, "products/detail.html", {"object" : obj})

#misal product tidak ada
def product_api_detail__view(request, id):
    # try:
    #     obj = Products.objects.get(id=id)
    # except Products.DoesNotExist:
    #     raise Http404
    try:
        obj = Products.objects.get(id=id)
    except:
        raise Http404

    return JsonResponse({'id':obj.id})
