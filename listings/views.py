from django.http import JsonResponse

def sample_listing(request):
    return JsonResponse({"message": "Hello from listings app!"})
