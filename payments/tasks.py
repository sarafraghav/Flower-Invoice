from celery.decorators import task
from celery.utils.log import get_task_logger
from time import sleep
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
logger = get_task_logger(__name__)

@task(name='my_first_task')
def my_first_task(duration):
    sleep(duration)
    return('first_task_done')




@task(name='mail_sender')
def mail_sender(mail_subject,message,to_email):
  email = EmailMessage(mail_subject, message, to=[to_email])
  email.send()
  return('Email Sent')