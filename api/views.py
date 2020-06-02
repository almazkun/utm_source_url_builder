from django.http import JsonResponse
import json
# Create your views here.
from .models import Receiver
from .utils import send_email

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def api_receiver(request):
    if request.method == "POST":
        received_json_data = json.loads(request.body.decode("utf-8"))
        send_email(received_json_data)
        return JsonResponse({"Status": "Success"})
    return JsonResponse({"Status": "Error"})