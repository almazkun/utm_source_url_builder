from django.conf import settings
from django.core.mail import send_mail



def send_email(email_request):
    subject = "API_endpoint_used"
    message = str(email_request)
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email_from]
    send_mail(subject, message, email_from, recipient_list)
    print("mail sent", subject, message, email_from, recipient_list)
