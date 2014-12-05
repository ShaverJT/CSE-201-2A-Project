from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.contrib.auth.decorators import login_required

from Applications.models import App, Review
from Applications.forms import ReviewForms, AppForms

def index(request):
    latest_app_list = App.objects.filter(approved=True).order_by('-pub_date')
    context = {'latest_app_list': latest_app_list, 'logged_in': request.user.is_authenticated()}
    return render(request, 'Applications/index_ext.html', context)

def detail(request, app_id):
    app = get_object_or_404(App, pk=app_id)
    if app.approved:
        return render(request, 'Applications/detail_ext.html', {'app': app, 'logged_in': request.user.is_authenticated()})
    elif request.user.is_staff:
        return render(request, 'Applications/detail_ext.html', {'app': app, 'logged_in': request.user.is_authenticated()})
    return index(request)

@login_required()
def add_review(request, app_id):
    app = App.objects.get(id=app_id)
    if request.POST:
        review = Review(app=app)
        form = ReviewForms(request.POST, instance=review)
        form.save()
        
        return detail(request, app_id)
    
    return render(
        request,
        'Applications/add_review.html',
        {
            'logged_in': request.user.is_authenticated(),
            'form': ReviewForms,
            'app': app,
        }
    )

@login_required()
def submit(request):
    if request.POST:
        form = AppForms(request.POST)
        app = form.save()
        
        return detail(request, app.id)
    
    return render(
        request,
        'Applications/submit.html',
        {
            'logged_in': request.user.is_authenticated(),
            'form': AppForms,
        }
    )