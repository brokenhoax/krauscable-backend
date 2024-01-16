from django.shortcuts import render
from django.http import HttpResponse


# Create your views (aka 'request handler') here.
def say_hello(request):
    x = 1
    y = 2
    print(y)
    return render(request, "hello.html", {"name": "Andrew"})
