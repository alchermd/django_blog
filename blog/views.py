from django.http import HttpResponse


def home(request):
    return HttpResponse('Hello, World!')


def about(request):
    return HttpResponse('Hello from the about page!')
