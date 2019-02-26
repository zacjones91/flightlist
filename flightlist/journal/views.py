from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404, get_list_or_404, redirect
from django.template import RequestContext
from django.urls import reverse
from journal.models import *

def landing_page(request):

    return render(request, 'index.html')