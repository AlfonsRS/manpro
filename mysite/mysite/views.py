from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.shortcuts import render
from django.contrib import messages
from django.core.mail import send_mail
from . import forms

def welcome(request):
	return render(request, 'welcome.html')

def usermanagement(request):
	return render(request, 'usermanagement.html')

def notif(request):
	return render(request, 'notif.html')
	
def teammanagement(request):
	return render(request, 'teammanagement.html')

def profile(request):
	return render(request, 'profile.html')


@login_required
def contact(request):
	form = forms.ContactForm()
	if request.method == "POST":
		form = forms.ContactForm(request.POST)
		if form.is_valid():
			#Mengirim email
			send_mail(
				'Dari Kontak Rekan',
				request.POST['subject'],
				request.user.email,
				[request.POST['email']],
				fail_silently=False
			)
			messages.success(request, 'Email sent successfully!')
			return HttpResponseRedirect(reverse('contact'))

	return render(request, 'contact.html', {'form': form})