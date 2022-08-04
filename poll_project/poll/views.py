from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Poll
from .forms import CreateForm

# Create your views here.

def index(request):
	polls = Poll.objects.all()
	context = {
		"polls": polls
	}
	return render(request, "poll/index.html", context)

def create(request):
	if request.method == 'POST':
		form = CreateForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('index')
	else:
		form = CreateForm
	context ={
		"form": form
	}
	return render(request, "poll/create.html", context)

def vote(request, poll_id):
	poll = Poll.objects.get(pk=poll_id)
	if request.method == 'POST':
		selected_option = request.POST['poll']

		if selected_option == 'option1':
			poll.option1_checked +=1
		elif selected_option == 'option2':
			poll.option2_checked +=1
		elif selected_option == 'option3':
			poll.option3_checked +=1
		else:
			return HttpResponse(400, 'invalid form')
		poll.save()
		return redirect('results', poll.id)
	context ={
		"poll": poll
	}
	return render(request,"poll/vote.html", context)

def results(request, poll_id):
	poll = Poll.objects.get(pk=poll_id)
	context = {
		"poll": poll
	}
	return render(request, "poll/result.html", context)
