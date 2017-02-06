from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.contrib.auth import logout


def logout_view(request):
    logout(request)


def base(request):
    html = TemplateResponse(request, 'base.html')
    return HttpResponse(html.render())


def home(request):
    html = TemplateResponse(request, 'home.html')
    return HttpResponse(html.render())
