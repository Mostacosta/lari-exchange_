from django.shortcuts import render
from .models import contact_info,jobs
from django.shortcuts import get_object_or_404
from .forms import contact_form,job_form
from django.core.mail import EmailMessage


# Create your views here.
def contact_view (request):
    if request.session.get('lang') == False:
        request.session['lang'] = 'eng'
    lang = request.session.get('lang')
    my_contacts = get_object_or_404(contact_info, tag=lang)
    form  = contact_form()
    message = ""
    if request.method == 'POST':
        form = contact_form(request.POST)
        if form.is_valid():
            username=request.POST["name"]
            phone=request.POST["phone"]
            email=request.POST["email"]
            msg=request.POST["message"]
            mail_subject = "Email from "+username+" his phone number is "+phone+" and mail is "+email
            email = EmailMessage(
                mail_subject, msg, to=["mostafaelhassan910@gmail.com"]
            )
            email.send()
            form.save()
            message = "Thank you for your message, Lari staff will contact you!"
        else :
            message = form.errors.as_text()
    return render (request,'contacts/contact.html',{"contact":my_contacts,'form':form,'message':message})
    
def job_view (request):
    jobs_ = jobs.objects.all()
    if request.method =='POST':
        form = job_form(request.POST)
        if form.is_valid():
            job = request.POST["job"]
            info = request.POST["info"]
            username=request.POST["name"]
            gender = request.POST["gender"]
            date = request.POST["Date"]
            nationality = request.POST["Nationality"]
            qualifications = request.POST["Qualifications"]
            experience = request.POST["Experience"]
            phone=request.POST["Mobile Number"]
            email=request.POST["email"]
            mail_subject = "Email from "+username+" his phone number is "+phone+" and mail is "+email
            msg = job + "\n" + info + "\n" + gender + "\n" + date + "\n" + nationality + "\n" +qualifications + "\n" + experience
            email = EmailMessage(
                    mail_subject, msg, to=["mostafaelhassan910@gmail.com"]
                )
            email.send()
        
    return render (request,'contacts/career.html',{"jobs":jobs_})
