from django.core.mail import EmailMessage
from django.template.loader import render_to_string


def mail_sender(user,mail_subject,message,to_email,template)
  message = render_to_string(template, {'user': user,'message': message,})
  email = EmailMessage(mail_subject, message, to=[to_email])
  email.send()