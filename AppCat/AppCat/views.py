from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.utils import timezone


from Applications.models import App
from Applications.views import detail

def home(request):
    latest_app_list = App.objects.filter(approved=True).order_by('-pub_date')[:4]
    context = {'latest_app_list': latest_app_list}
    return render(request, 'Applications/welcome_ext.html', {'latest_app_list': latest_app_list, 'logged_in':request.user.is_authenticated()})

def about(request):
    return render(request, 'Applications/about_ext.html', {'logged_in': request.user.is_authenticated()})

def login_user(request):
	error = 'Please log in below...'
	username = ''
	logged_in = False

	if request.user.is_authenticated():
		error = 'You are already logged in'
		logged_in = True

	if request.POST:
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = authenticate(username=username, password=password)
		if user is not None:
			if user.is_active:
				login(request, user)
                                return HttpResponseRedirect("/")
			else:
				error = 'Your account is not active, please contact the site admin.'
				alert_level = 'warn'
		else:
			error = 'Your username and/or password were incorrect.'
			alert_level = 'alert'

	return render(
		request,
		'Applications/login.html',
		{
			'error_message': error,
			'username': username,
			'logged_in': logged_in,
		}
	)


def search(request):
    query = request.GET.get('query', '').lower()
    
    apps = App.objects.all()
    apps = filter(lambda x : query in x.app_name.lower() or query in x.description.lower(), apps)

    return render(
    	request,
    	'Applications/search.html',
    	{
    		'results': apps,
    		'query': query,
    		'logged_in': request.user.is_authenticated(),
	}
	)

def logout_user(request):
	logout(request)
	return home(request)

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect("/")
    else:
        form = UserCreationForm()
    return render(request, "Applications/signup.html", {
        'form': form,
    })

def approve(request):
    unapproved_apps = App.objects.filter(approved=False).order_by('-pub_date')
    context = {'unapproved_apps': unapproved_apps, 'logged_in': request.user.is_authenticated()}
    return render(request, "Applications/approve.html", context)

def update_approval(request, app_id, choice):
    app = App.objects.get(id=app_id)
    if choice=='0':
        
        app.delete()
        return approve(request)
    else:
        app.approved=True
        app.pub_date=timezone.now()
        app.save()
        return approve(request)
    
    
#def detail(request, app_id):
#    app = get_object_or_404(App, pk=app_id)
#    return render(request, 'Applications/detail.html', {'app': app})

#def reviews(request, app_id):
#    return HttpResponse("Reviews for Question %s." % app_id)
