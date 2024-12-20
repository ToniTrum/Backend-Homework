from django.shortcuts import render, HttpResponse
from .models import Model
from django.views.decorators.csrf import csrf_exempt

def main(request):
    return HttpResponse("""<form method='POST' action='/create/'>
                            <input type='text' name='content'>
                            <button type='submit'>Submit</button>
                        </form>""")

def get_all_contents(request):
    contents = Model.objects.all()
    content_list = [str(content) for content in contents]
    return HttpResponse(", ".join(content_list))

def get_content(request, content_id):
    try:
        content = Model.objects.get(id=content_id)
        return HttpResponse(content)
    except Model.DoesNotExist:
        return HttpResponse("Content not found")

@csrf_exempt
def create(request):
    if request.method == 'POST':
        content = request.POST.get("content")
        Model.objects.create(content=content)
        return HttpResponse(f"Success: {content}")
