from django.db.models.signals import post_save
from .models import Task
from django.dispatch import receiver


@receiver(post_save, sender=Task)
def assigneecheck(sender, instance, created, **kwargs):
    if created:
        check = instance.assignee.all()
        if not check:
            u1 = instance.owner
            instance.assignee.add(u1)
