from celery import shared_task
from connectors.resend import OnboardingEmail
from django.contrib.auth.models import User
@shared_task
def send_onboarding_email(user_id):
    user = User.objects.get(id=user_id)
    email = OnboardingEmail(user)
    email.send()