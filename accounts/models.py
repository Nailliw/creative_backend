from django.db import models
from django.contrib.auth.models import User


def upload_image(instance, filename):
    return f"{instance.name}-{instance.user.username}"


class Archive(models.Model):
    name = models.TextField(max_length=255)
    file = models.ImageField(upload_to="", blank=True, null=False)
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Person",
        related_name="files",
    )
