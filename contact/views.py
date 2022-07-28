from django.http import HttpResponseRedirect
from django.shortcuts import render
# from .forms import ContactForm
from .models import Contacts

# Create your views here.
def contact(request):
    context={}
    if request.method =="POST":
        print(request.POST)
        title=request.POST.get("name")
        print(title)
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        subject = request.POST.get("subject")
        
        contact_obj = Contacts.objects.create(name=name, email=email, message=message, subject=subject)
        
        context['contact_obj'] = contact_obj
        
        # context['created'] = True
        
    
    
      
    return render(request,    
            'articles/contact.html', 
            context=context)