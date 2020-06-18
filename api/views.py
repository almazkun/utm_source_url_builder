from django.http import JsonResponse
import json
# Create your views here.
from .models import Receiver
from .utils import send_email

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_receiver(request):
    send_email(f"{request.META}, {request.body.decode('utf-8')}")
    if request.method == ("POST" or "GET"):
        return JsonResponse({"Status": "Success"})
    return JsonResponse({"Status": "Error"})