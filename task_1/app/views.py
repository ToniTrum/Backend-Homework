from django.shortcuts import render, HttpResponse

def about(request):
    return HttpResponse("<h1>About</h1>")

def main(request):
    return HttpResponse("<h1>Main</h1>")