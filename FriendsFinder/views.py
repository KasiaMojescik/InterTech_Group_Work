from django.shortcuts import render
from FriendsFinder.forms import UserForm, UserProfileForm
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from datetime import datetime
from django.template import RequestContext
from django.shortcuts import render_to_response

#SITE MAP
#Index -> Register
#Index -> Login
#TODO
#Logged in Index, Forum home, Thread Rendering, Add comment Page, ????
def index(request):
	context_dict = {}
	response = render(request, 'FriendsFinder/index.html', context=context_dict)

	return response

#Potentially re-usable existing code?
def about(request):
	context_dict = {}
	response = render(request, 'FriendsFinder/about.html', context=context_dict)

	return response

def register(request):
#A boolean value for telling the template whether the registration was successful.
#Set to False initially. Code changes value to True when registration succeeds.
	registered = False

	#If it's a HTTP POST we attempt to process sent data
	if request.method == 'POST':
		#Attempt to grab information from the raw form information. (NOTE: we use both UserForm and UserProfileForm)
		user_form = UserForm(data=request.POST)
		profile_form = UserProfileForm(data=request.POST)

		#Check form validity
		if user_form.is_valid() and profile_form.is_valid():
			user = user_form.save()
			user.set_password(user.password)
			user.save()

			#Set commit to False until we sort potential data integrity problem then commit fully
			profile = profile_form.save(commit=False)
			profile.user = user
			profile.save()

			#Successful registration
			registered = True
		else:
			#Generic for now just print errors rather than sort
			print(user_form.errors, profile_form.errors)
	else:
        #Not HTTP Post, so we render our registration forms
		user_form = UserForm()
		profile_form = UserProfileForm()

    #Render template depending on content (primarily depends on value of registered
	return render(request,
		'FriendsFinder/register.html',{'user_form': user_form, 'profile_form': profile_form, 'registered': registered})
		
def user_login(request):
    #If POST request then extract information from POST parameters
	if request.method == 'POST':

# Gather the username and password provided by the user.
# This information is obtained from the login form.
# We use request.POST.get('<variable>') as opposed
# to request.POST['<variable>'], because the
# request.POST.get('<variable>') returns None if the
# value does not exist, while request.POST['<variable>']
# will raise a KeyError exception.
		username = request.POST.get('username')
		password = request.POST.get('password')
# Use Django's machinery to attempt to see if the username/password
# combination is valid - a User object is returned if it is.
		user = authenticate(username=username, password=password)
# If we have a User object, the details are correct.
# If None (Python's way of representing the absence of a value), no user
# with matching credentials was found.
		if user:
# Is the account active? It could have been disabled.
			if user.is_active:
# If the account is valid and active, we can log the user in.
# We'll send the user back to the homepage.
				login(request, user)
				return HttpResponseRedirect(reverse('index'))
			else:
# An inactive account was used - no logging in!
				return HttpResponse("Your Friends Finder account is disabled.")
		else:
# Bad login details were provided. So we can't log the user in.
			print("Invalid login details: {0}, {1}".format(username, password))
			return HttpResponse("Invalid login details supplied.")
# The request is not a HTTP POST, so display the login form.
# This scenario would most likely be a HTTP GET.
	else:
# No context variables to pass to the template system, hence the
# blank dictionary object...
		return render(request, 'FriendsFinder/login.html', {})
		
@login_required
def quiz(request):
	return render(request, 'FriendsFinder/quiz.html', {})
	
# Use the login_required() decorator to ensure only those logged in can
# access the view.
@login_required
def user_logout(request):
# Since we know the user is logged in, we can now just log them out.
	logout(request)
# Take the user back to the homepage.
	return HttpResponseRedirect(reverse('index'))
	
# Updated the function definition
def visitor_cookie_handler(request):
	visits = int(get_server_side_cookie(request, 'visits', '1'))
	last_visit_cookie = get_server_side_cookie(request,
												'last_visit',
												str(datetime.now()))
	last_visit_time = datetime.strptime(last_visit_cookie[:-7],
												'%Y-%m-%d %H:%M:%S')
# If it's been more than a day since the last visit...
	if (datetime.now() - last_visit_time).days > 0:
		visits = visits + 1
#update the last visit cookie now that we have updated the count
		request.session['last_visit'] = str(datetime.now())
	else:
		visits = 1
		# set the last visit cookie
		request.session['last_visit'] = last_visit_cookie
	# Update/set the visits cookie
	request.session['visits'] = visits
	
# A helper method
def get_server_side_cookie(request, cookie, default_val=None):
	val = request.session.get(cookie)
	if not val:
		val = default_val
	return val