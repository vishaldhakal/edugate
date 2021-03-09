
from django.conf import settings
from django.dispatch import receiver
from django.db.models.signals import post_delete
from .models import Lesson,Topic,Course

# By adding 'Lesson' as 'sender' argument we only receive signals from that model
@receiver(post_delete, sender=Lesson)
def on_delete(sender, **kwargs):
    instance = kwargs['instance']
    # video is the name of the field file of the Lesson model
    instance.video.delete(save=False)