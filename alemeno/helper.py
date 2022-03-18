from django.http import request
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage, send_mail
from django.template.loader import render_to_string
from .models import Kid

def sendEmail(user, mail_subject, template, kid_id, kid):
  mail_Id = Kid.objects.get(id=kid_id)
  exact_Email = mail_Id.parent_email
  message = render_to_string(template, {
    'user': user,
    'kid': kid,
  })
  to_email = exact_Email
  #To use in local host, uncomment below 2 lines, except the last one.
  send_email = EmailMessage(mail_subject, message, to=[to_email])
  mail = send_email.send()
  # print(send_email.send())
  # print('Status is on your above')
  # mail = send_mail(mail_subject, message, 'accounts@golaghatiti.org', [to_email], fail_silently=False,)
  # return mail