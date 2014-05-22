from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext, loader

def smart_power_nap(request):
    return render(request, 'website/blogs/smartpowernap.html', {})
