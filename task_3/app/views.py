from django.shortcuts import render, HttpResponse, HttpResponseRedirect
from .models import Model
from django.views.decorators.csrf import csrf_exempt

def main(request):
    contents = Model.objects.all()
    content_list = [str(content) for content in contents]
    return HttpResponse(f"""<form method='POST' action='/contents/'>
                            <input type='text' name='content'>
                            <button type='submit'>Post</button>
                        </form>
                        <form method='GET' action='/contents/'>
                            <input type='number' name='id'>
                            <button type='submit'>Get</button>
                        </form>""")

@csrf_exempt
def contents(request):
    if request.method == 'POST':
        content = request.POST.get("content")
        Model.objects.create(content=content)
        return HttpResponseRedirect('/')
    if request.method == 'GET':
        try:
            content_id = request.GET.get("id")
            content = Model.objects.get(id=content_id)
            return HttpResponse(content)
        except Model.DoesNotExist:
            return HttpResponse("Content not found")