from django.shortcuts import render
from django.http import HttpResponse
from .forms import StudentForm
from .forms import FeedbackForm
# Create your views here.

def index(request):
	form = StudentForm(request.POST or None)
	context = {
	   "hello_message" : "Register new student",
	   "form" : form

	}

	if form.is_valid():
		instance = form.save(commit = False)
		full_name = form.cleaned_data.get('full_name')
		if full_name == "lue":
			full_name = "Developer"
		instance.full_name = full_name
		instance.save()

		context = {
		    "hello_message": "Student saved"
		}
	
	return render(request, 'index.html', context)
def feedback(request):
	form = FeedbackForm(request.POST or None)
	if form.is_valid():
        from_email = form.cleaned_data.get('email')
        full_name = form.cleaned_data.get('full_name')
        message form.cleaned_data.get('message')
        prepared_message = "You have feedback form {} saying '{}'".format(full_name, message)

        send_mail('New feedback', prepared_message, from_email,
    ['to@example.com'], fail_silently=False)
		#for key, value in form.cleaned_data.items():
			#print(key, value)

	context = {
	   "form" : form
	}
	return render(request, 'feedback.html', context)
