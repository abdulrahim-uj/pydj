import os.path
import re
import string
import random
from django.http import HttpResponse
from decimal import Decimal

import shutil


from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from django.conf import settings


def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip


def generate_unique_id(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))


def generate_form_errors(args, formset=False):
    message = ''
    if not formset:
        for field in args:
            if field.errors:
                message += field.errors + "|"
        for err in args.non_field_errors():
            message += str(err) + "|"

    elif formset:
        for form in args:
            for field in form:
                if field.errors:
                    message += field.errors + "|"
            for err in form.non_field_errors():
                message += str(err) + "|"
    return message[:-1]


def get_auto_id(model):
    auto_id = 1
    latest_auto_id = model.objects.all().order_by("-sended_at")[:1]
    if latest_auto_id:
        for auto in latest_auto_id:
            auto_id = auto.auto_id + 1
    return auto_id


def get_timezone(request):
    if "set_user_timezone" in request.session:
        user_time_zone = request.session['set_user_timezone']
    else:
        user_time_zone = "Asia/Kolkata"
    return user_time_zone


def send_response_mail(request, contacter, to_email, regarding, company, mail_subject, mail_template, attachement):
    current_site = get_current_site(request)
    message_body = render_to_string(mail_template, {
        'who_is_contact': contacter,
        'regarding': regarding,
        'my_name': attachement.profile.name.title(),
    })
    to_email = to_email
    mail = EmailMessage(subject=mail_subject, body=message_body,
                        from_email=settings.DEFAULT_FROM_EMAIL,
                        to=[to_email], cc=[settings.DEFAULT_CC_EMAIL], bcc=[settings.DEFAULT_BCC_EMAIL])

    cover = attachement.cover_letter.path
    cover_name = "cover_letter_for_"+company+".txt"
    shutil.copy(cover, cover_name)
    with open(cover_name, 'r') as file:
        filedata = file.read()
    # Replace the target string
    filedata = filedata.replace('[Name]', contacter)
    filedata = filedata.replace('[Junior Software Developer] ', regarding + " ")
    filedata = filedata.replace('[Company Name].', company + ".")
    # Write the file out again
    with open(cover_name, 'w') as file:
        file.write(filedata)

    mail.attach_file(attachement.resume_file.path)
    mail.attach_file(cover_name)

    mail.content_subtype = "html"
    mail.send()
#     remove created file
    if os.path.exists(cover_name):
        os.remove(cover_name)
