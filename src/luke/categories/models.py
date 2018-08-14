from django.contrib.auth.models import User

from django.db import models

from luke.core.db.models import TimeStampedMixin


class Category(TimeStampedMixin):
    title = models.CharField(max_length=255)
    active = models.BooleanField(null=False, default=True)

    # Relations
    user = models.ForeignKey(User, related_name='categories')
