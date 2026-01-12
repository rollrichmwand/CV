from django.shortcuts import render, redirect
from django.core.mail import send_mail
from .models import Profile
from django.conf import settings
from .forms import ContactForm



def home(request):
    profile = Profile.objects.first()
    form = ContactForm()
    
    if request.method=='POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = form.save()
            send_mail(subject=f"New message from {message.name}", message=message.message, 
            from_email=settings.DEFAULT_FROM_EMAIL, recipient_list=[profile.email], fail_silently=True)
        return redirect('home')
    return render(request, 'myCv/home.html', {'profile': profile, 'form': form},)