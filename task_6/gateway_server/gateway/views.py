import requests
from django.http import JsonResponse

def proxy_request(request):
    try:
        url = "http://127.0.0.1:8000/"
        response = requests.get(url)
        return JsonResponse(response.json(), status=response.status_code)
    except requests.RequestException as e:
        return JsonResponse({"error": "Failed to connect to the first server", "details": str(e)}, status=500)
