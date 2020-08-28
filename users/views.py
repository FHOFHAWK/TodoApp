from django.http import HttpResponse


def index(request):
    return HttpResponse("Не знаю почему, но всё работает:D")
