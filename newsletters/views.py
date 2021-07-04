from django.shortcuts import render
from django.contrib import messages

from .models import Newsletter
from .forms import NewsletterForm


def subscribe_newsletter(request):
    """ Subscribe Newsletter """

    if request.method == 'POST':
        newsletter_form = NewsletterForm(request.POST)
        if newsletter_form.is_valid():
            newsletter_form.save()
            messages.success(request, 'Thank you very much for subscribing to our newsletter')
    else:
        newsletter_form = newsletter_form()

    context = {
        'form': newsletter_form
    }

    return render(request, 'home/index.html', context)
