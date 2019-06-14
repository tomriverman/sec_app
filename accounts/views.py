from django.shortcuts import render
from django.contrib.auth import login, get_user_model, logout, user_logged_in

from django.http import HttpResponseRedirect
# Create your views here.
from .forms import UserCreationForm, UserLoginForm
from django.contrib.auth.decorators import login_required

@login_required
def register(request, *args, **kwargs):
	form = UserCreationForm(request.POST or None)
	if form.is_valid():
		form.save()
		return HttpResponseRedirect('/login')
	context = {
		'form': form
	}
	return render(request, "accounts/register.html", context)


def login_view(request, *args, **kwargs):
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        user_obj = form.cleaned_data.get('user_obj')
        login(request, user_obj)
        if request.user.is_livr:
            return HttpResponseRedirect("/delivery")
        else:
            return HttpResponseRedirect("/")
    return render(request, "accounts/login.html", {"form": form})

@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect("/login")
