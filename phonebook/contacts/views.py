from django.shortcuts import render, get_object_or_404,redirect
from django.http import HttpResponseRedirect
from django.urls import reverse
from . models import Contact
from . forms import ContactForm
from typing import List
from django.db.models import Q
from django.views.generic import (UpdateView)

# Create your views here.
def add_contacts(request):
    all_conts = Contact.objects.all()
    list_name = []
    list_number = []
    for i in all_conts:
        list_name.append(i.name)
        list_number.append(i.phone_number)

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            phone_number = form.cleaned_data['phone_number']
            if name not in list_name and phone_number not in list_number:
                form.save()
                a = Contact.objects.get(name=name)
                return HttpResponseRedirect(reverse(details, kwargs={'pk': a.id}))
            else:
                context = {
                    'form': form,
                    'error': "name or number already exists"
                }
                return render(request, "contacts/index.html", context)
    form = ContactForm()
    return render(request, "contacts/index.html", {'form': form})

def details(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    context = {
        'contact': contact
    }
    return render(request, "contacts/details.html", context)

def all(request):
    all_conts = Contact.objects.all()
    list_conts: List[Contact] = []
    for i in all_conts:
        list_conts.append(i)
    ordered_list = sorted(list_conts, key=lambda con: con.name)
    context = {"all_conts": ordered_list}
    return render(request, "contacts/contacts.html", context)

def update(request, pk):
    all_conts = Contact.objects.all()
    list_name = []
    list_number = []
    for i in all_conts:
        list_name.append(i.name)
        list_number.append(i.phone_number)
    contact = get_object_or_404(Contact, id=pk)
    if request.method == 'GET':
        form = ContactForm(initial={
            'name': contact.name,
            'phone_number': contact.phone_number,
        })
        context = {
            'form': form,
            'contact': contact
                   }
        #return render(request, 'contacts/index.html', context)
        return render(request, 'contacts/update.html', context)
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact.name = form.cleaned_data['name']
            contact.phone_number = form.cleaned_data['phone_number']
            #if form.cleaned_data['name'] not in list_name and form.cleaned_data['phone_number'] not in list_number:
            contact.save()
            context = {
                "contact": contact,
                "form": form,
            }
            return HttpResponseRedirect(reverse(details, kwargs={'pk': contact.id}))
            #return redirect(reverse('allcontacts'))
                #return redirect(reverse('details'))
                #return render(request, 'contacts/update.html', context)
                #return HttpResponseRedirect(reverse(details, kwargs={'pk': a.id}))
        return render(request, "contacts/update.html", {"form": form})
        #return HttpResponseRedirect(reverse(details, kwargs={'pk': contact.id}))
        #form = ContactForm()
        #return render(request, "contacts/update.html", {'form': form})
def search(request):
    query = request.POST.get('q')
    result = get_object_or_404(Contact, Q(name__icontains=query))
    #result = Contact.objects.filter(Q(name__icontains=query))
    #return render(request, 'contacts/search.html', {'result': result})
    return redirect(details, pk=result.id)

def delete(request, pk):
    contact = get_object_or_404(Contact, id=pk)
    contact.delete()
    return redirect('allcontacts')

