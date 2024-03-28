from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Reference, ContactInfo, Service, CustomerDetails
from django.core.mail import send_mail
from django.db.models import Avg, Count
from django.conf import settings
from django.core.mail import send_mail

def home_page(request):
    return render(request, 'home_page.html', {})

def reference_list(request):
    references = Reference.objects.all()
    return render(request,'reference_list.html', {'references': references})

def contact_info(request):
    contact_info = ContactInfo.objects.first()  
    return render(request, 'contact_info.html', {'contact_info': contact_info})

def services(request):
    services = Service.objects.all()
    return render(request, 'services.html', {'services': services})

def order_services(request):
    if request.method == 'POST':
        order = CustomerDetails(request.POST)
        if obrazec.is_valid():
            obrazec.save()
            messages.success(request, 'Vaš obrazec je bil uspešno poslan. Kontaktirali vas bomo v kratkem.')
            return redirect('domaca_stran')
    else:
        obrazec = CustomerDetails(initial={'ime': '', 'email': '', 'telefonska_stevilka': '', 'vas_avto': '', 'storitev': '', 'sporocilo': ''})
    active_page = 'kontakt_obrazec'
    return render(request, 'kontakt_obrazec.html', {'obrazec': obrazec, 'active_page': active_page})


def order_confirmation(request):
    if request.method == "POST":
        ime = request.POST['ime']
        email = request.POST['email']
        telefon = request.POST['telefon']
        sporocilo = request.POST['sporocilo']

        # Format the email message
        message = f"Ime in priimek: {ime}\nE-pošta: {email}\nTelefon: {telefon}\nStoritev: \nSporočilo: {sporocilo}"

        send_mail(
            subject="Nova stranka pošilja povpraševanje",
            message=message,
            from_email=settings.EMAIL_HOST_USER,
            recipient_list=['tlakipikelj@gmail.com'],
        )
        
        return render(request, 'order_confirmation.html', {
            'ime': ime,
            'email': email,
            'telefon': telefon,
            'sporocilo': sporocilo, 
        })
    else:
        return render(request, 'domaca_stran.html', {})
