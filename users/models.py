from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _



class CustomUser(AbstractUser):
    USER_TYPES = (
        ('coordinator', 'Coordinator'),
        ('room_keeper', 'Room Keeper'),
        ('student', 'Student'),
        ('teacher', 'Teacher')
    )

    status = models.CharField(max_length=12,
                              choices=USER_TYPES,
                              default='waiting')

    def __str__(self):
        return self.username