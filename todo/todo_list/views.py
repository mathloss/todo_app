from django.shortcuts import render, redirect
from .models import Liste 
from .forms import ListForm
from django.contrib import messages
from django.http import HttpResponseRedirect

def home(request):

	if request.method == "POST":
		form = ListForm(request.POST or None)

		if form.is_valid():
			form.save()
			les_items = Liste.objects.all
			messages.success(request,('Un élément a été ajouté à la liste!!'))
			return render(request, 'home.html', {'les_items':les_items})

	else:
		les_items = Liste.objects.all
		return render(request, 'home.html', {'les_items':les_items})

def apropos(request):
	mon_nom = "Mathieu"
	return render(request, 'apropos.html', {'nom':mon_nom})

def delete(request, list_id):
	item = Liste.objects.get(pk=list_id)
	item.delete()
	messages.success(request,('Un élément a été effacé de la liste!!'))
	return redirect('home')

def cocher(request, list_id):
	item = Liste.objects.get(pk=list_id)
	item.completed = True
	item.save()
	return redirect('home')

def decocher(request, list_id):
	item = Liste.objects.get(pk=list_id)
	item.completed = False
	item.save()
	return redirect('home')

def editer(request,list_id):
	if request.method == "POST":
		item = Liste.objects.get(pk=list_id)
		form = ListForm(request.POST or None, instance=item)

		if form.is_valid():
			form.save()			
			messages.success(request,('Un élément a été édité!!'))
			return redirect('home')

	else:
		item = Liste.objects.get(pk=list_id)
		return render(request, 'editer.html', {'item':item})