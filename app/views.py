from django.http import HttpResponse


def index(request):
    return  HttpResponse("Very Nice")

# Create your views here.
