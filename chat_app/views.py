from django.shortcuts import render, HttpResponse
from django.http import HttpRequest
from .models import Profile, Friend
from .forms import ChatMessageForm

# Create your views here.

def index(request):
	user = request.user.profile
	friends = user.friends.all()
	context = {
		'user':user,
		'friends':friends,
	}
	return render(request, 'index.html', context)


def detail(request, pk):
	user = request.user.profile
	friend = Friend.objects.get(profile_id=pk)
	form = ChatMessageForm()
	context = {
		'friend':friend,
		'user':user,
		'form':form,
	}
	return render(request, 'detail.html', context)