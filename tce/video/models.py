from django.db import models
from django.dispatch import receiver
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.conf import settings
# Create your models here.


class Video(models.Model):
    caption = models.CharField(max_length=100)
    video = models.FileField(upload_to="video/%y")

    def __str__(self):
        return self.caption


@receiver(post_delete, sender=Video)
def submission_delet(sender, instance, **kwargs):
    instance.video.delete(False)
