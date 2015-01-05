from django.shortcuts import render, get_object_or_404, redirect
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.core.mail import send_mail
from ek_site.forms import ContactForm
# Create your views here.
def index(request):
    return render(request, 'ek_site/index.html')

def about(request):
    return render(request, 'ek_site/about.html')

def thanks(request):
    return render(request,'ek_site/thanks.html')

def projects(request):
    return render(request, 'ek_site/projects.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request._post)
        if form.is_valid():
            cleaned = form.cleaned_data
            sender = cleaned['sender']
            subject = cleaned['subject']
            message = cleaned['message']
            message += ' Sent from: ' + sender
            send_mail(
                subject,
                message,
                sender,
                {'ellingtonkirby31@gmail.com'}
            )
            return redirect('thanks')
    else:
        form = ContactForm()
    return render(request,'ek_site/contact.html', {'form': form})

