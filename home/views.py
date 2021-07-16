from django.shortcuts import render
from django.contrib import messages

from .forms import SubscriptionForm


def index(request):
    """ A view to return the index page """

    return render(request, 'home/index.html')
