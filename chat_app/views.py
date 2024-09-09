from django.shortcuts import render, HttpResponse, redirect
from django.http import HttpRequest
from .models import Profile, Friend, ChatMessage
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
	profile = Profile.objects.get(id=friend.profile.id)
	chats = ChatMessage.objects.all()
	form = ChatMessageForm()
	if request.method == "POST":
		form = ChatMessageForm(request.POST)
		if form.is_valid:
			chat_message = form.save(commit=False)
			chat_message.msg_sender = user
			chat_message.msg_receiver = profile
			chat_message.save()
			#return redirect(request.META.get("HTTP_REFERER"))
			return redirect("detail", pk=friend.profile.id)
	context = {
		'friend':friend,
		'user':user,
		'form':form,
		'profile':profile,
		'chats':chats,
	}
	return render(request, 'detail.html', context)