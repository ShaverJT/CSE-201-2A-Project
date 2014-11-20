from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404

from Applications.models import App

def index(request):
    latest_app_list = App.objects.order_by('-pub_date')[:5]
    context = {'latest_app_list': latest_app_list}
    return render(request, 'Applications/index.html', context)

#def index(request):
 #   return HttpResponse("fucking work")                                                                                                                                             
  #  latest_app_list = Applications.objects.all().order_by('-pub_date')[:5]
   # context = {'latest_app_list': latest_app_list}
    #return render(request, 'Applications/index.html', context)

def detail(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    return render(request, 'Applications/detail.html', {'app': app})

def reviews(request, app_id):
    return HttpResponse("Reviews for Question %s." % app_id)
