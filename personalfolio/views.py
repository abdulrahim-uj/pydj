from django.shortcuts import render, redirect
from . models import Profile, AboutUs, Experiance, Education, Skills, Services, Resume, Projects, HireMessage
from . forms import ContactUsForm
from . functions import get_auto_id, send_response_mail
from izitoast.functions import izitoast


def base(request):
    profile = Profile.objects.get(is_deleted=False)
    about_us = AboutUs.objects.get(is_deleted=False, profile=profile)
    experience = Experiance.objects.filter(is_deleted=False, profile=profile)
    education = Education.objects.filter(is_deleted=False, profile=profile)
    skills = Skills.objects.filter(is_deleted=False, profile=profile)
    services = Services.objects.filter(is_deleted=False, profile=profile)
    resume = Resume.objects.filter(is_deleted=False, profile=profile)
    projects = Projects.objects.filter(is_deleted=False, profile=profile)
    form_contact_me = ContactUsForm()
    context = {
        "title": "Portfolio",
        "base_script": True,
        "style_switcher": True,
        "typer": True,
        "disable_dev_tools": False,
        #
        "profiler": profile,
        "about": about_us,
        "exp": experience,
        "edu": education,
        "skill": skills,
        "services": services,
        "resume": resume,
        "projects": projects,
        "contact_me": form_contact_me,
    }
    return render(request, 'base/base.html', context)


def contact_me(request):
    if request.method == "POST":
        form = ContactUsForm(request.POST)
        resume_attachement = Resume.objects.get(is_deleted=False)
        if form.is_valid():
            contact = form.save(commit=False)
            contact.auto_id = get_auto_id(HireMessage)
            form.save()
            to_email = form.cleaned_data['email']
            regarding = form.cleaned_data['subject']
            contacter = form.cleaned_data['name']
            company_name = form.cleaned_data['company']
            # *
            email_subject = "Thank you for connecting me..."
            email_template = "hire/email-template.html"
            send_response_mail(request, contacter, to_email, regarding, company_name,
                               email_subject, email_template, resume_attachement)
            # >>

            message = "E-mail successfully send."
            diversify = {
                "position": "topRight",
                "transition_in": "flipInX",
                "transition_out": "flipOutX",
                "time_out": 3000,
            }
            izitoast(request=request, model="success",
                     message=message, diversify=diversify)
            return redirect('personalfolio:basePage')
        else:
            diversify = {
                "position": "topRight",
                "transition_in": "flipInX",
                "transition_out": "flipOutX",
                "time_out": 4000,
            }
            izitoast(request, "form-error", form.errors, diversify)
            return redirect('personalfolio:basePage')
