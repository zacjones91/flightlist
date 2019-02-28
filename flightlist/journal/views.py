from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext
from django.urls import reverse
from journal.models import *
from journal.forms import *


def landing_page(request):

    return render(request, 'index.html')


def register(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user as well as a new customer at the same time
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return login_user(request)

        else:
            print("not valid user form")

    elif request.method == 'GET':
        user_form = UserForm()
        context = {'user_form': user_form}
        template_name = 'register.html'
        return render(request, template_name, context)


def login_user(request):
    '''Handles the creation of a new user for authentication
    Method arguments:
      request -- The full HTTP request object
    '''

    # Obtain the context for the user's request.
    context = RequestContext(request)

    # If the request is a HTTP POST, try to pull out the relevant information.
    if request.method == 'POST':

        # Use the built-in authenticate method to verify
        username = request.POST['username']
        password = request.POST['password']
        authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
        if authenticated_user is not None:
            login(request=request, user=authenticated_user)
            return HttpResponseRedirect('journal')

        else:
            # Bad login details were provided. So we can't log the user in.
            print("Invalid login details: {}, {}".format(username, password))
            return HttpResponse("Invalid login details supplied.")

    return render(request, 'login.html', {}, context)

# Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)
    return HttpResponseRedirect('journal')

# ============================ Entries =========================== #


def all_entries(request, pk):

    all_entries = Entry.objects.filter(user_id=pk).order_by('date')
    context = {'all_entries': all_entries}
    return render(request, 'all_entries.html', context)

# get and create new


def new_entry(request, pk):

    if request.method == 'GET':
        journal_form = JournalForm()
        context = {'journal_form': journal_form}
        return render(request, 'new_entry.html', context)

    if request.method == 'POST':

        title = request.POST['title']
        content = request.POST['content']
        date = request.POST['date']
        image = request.POST['image']

        journal_to_save = Entry(
            title=title, date=date, content=content, image=image, user_id=request.user.id)
        journal_to_save.save()

        return HttpResponseRedirect(reverse('journal:all_entries', args=(request.user.id,)))

# detail view

def detail(request, pk):

    entry = Entry.objects.filter(id=pk)
    context = {'entry': entry}
    return render(request, 'detail.html', context)    


def edit_entry(request, pk):

    if request.method == 'GET':
        entry_to_edit = Entry.objects.get(id=pk)
        journal_form = JournalForm(
            initial={
                'title': entry_to_edit.title,
                'content': entry_to_edit.content,
                'date': entry_to_edit.date,
                'image': entry_to_edit.image
            }
        )
        context = {'journal_form': journal_form, 'entry_to_edit': entry_to_edit}
        return render(request, 'edit_entry.html', context)

    if request.method == 'POST':

        entry_to_edit = Entry.objects.get(id=request.POST['entry_id'])

        title = request.POST['title']
        content = request.POST['content']
        date = request.POST['date']
        image = request.POST['image']
        entry_id = request.POST['entry_id']

        journal_to_save = Entry(
            pk=entry_id, title=title, date=date, content=content, image=image, user_id=request.user.id)
        journal_to_save.save()

        return HttpResponseRedirect(reverse('journal:all_entries', args=(request.user.id,)))

#  delete an entry

def delete_entry(request, pk):
    to_delete = Entry.objects.get(id=pk)
    to_delete.delete()
    return HttpResponseRedirect(reverse('journal:all_entries', args=(request.user.id,)))