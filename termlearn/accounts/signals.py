from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User
from .models import Profile
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.core.mail import send_mail



@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:  # Only send email when a new user is created
        send_mail(
            'Welcome to TerminalLearn',
            f'Hi {instance.first_name}, welcome to TerminalLearn — your place to learn terminal commands!',
            'noreply@terminallearn.local',  # DEFAULT_FROM_EMAIL also works here
            [instance.email],
            fail_silently=True
        )
