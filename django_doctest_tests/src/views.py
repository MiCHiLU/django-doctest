from django.http import HttpResponse
from django.template import Context, Template
from django.views.generic.simple import direct_to_template

def render(request, *argv):
    t = Template(request.GET.get("source", " {{ DUMMY }} "))
    return HttpResponse(t.render(Context()))

def use_template(request, *argv):
    return direct_to_template(request, "sample.html", {})

