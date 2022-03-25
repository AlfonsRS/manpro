from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Blog, Comment
from django.urls import reverse
from django.contrib import messages
from . import forms

def handler404(request):
	return render(request, '404.html', status=404)

def index(request):
	blogs = Blog.objects.all()
	return render(request, 'blogs/index.html', {'blogs':blogs})

def single(request, id):
	blog = get_object_or_404(Blog,pk = id)
	form = forms.CommentForm()
	return render(request, 'blogs/single.html', {'blog':blog, 'form': form})

def comment(request, id):
	blog = get_object_or_404(Blog,pk = id)
	form = forms.CommentForm()

	if request.user.id != comment.user.id:
		return render(request, '404.html')

	if request.method == "POST":
		form = forms.CommentForm(request.POST)
		if form.is_valid():
			#Mengirim email
			newDesc = request.POST['desc']
			blog.comment_set.create(desc=newDesc, user=request.user)
			messages.success(request, 'berhasil submit komentar!')
			return HttpResponseRedirect(reverse('blogs:index'))
			
	return render(request, 'blogs/single.html', {'blog':blog, 'form': form})
		# blog.comment_set.create(desc=newDesc)
		# return HttpResponseRedirect('/blogs')

def comment_edit(request, id):
	comment = get_object_or_404(Comment ,pk = id)
	form = forms.CommentForm(instance=comment)
	

	if request.method == "POST":
		form = forms.CommentForm(instance = comment, data=request.POST)
		if form.is_valid():
			form.save()
			messages.success(request, 'komentar berhasil diupdate!')
			return HttpResponseRedirect(reverse('blogs:index'))

	return render(request, 'blogs/comment_edit.html', {'comment': comment, 'form': form})
