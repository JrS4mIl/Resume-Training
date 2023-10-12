from django.db import models

# Create your models here.
from django.db import models
from core.models import AbstractModel
# Create your models here.

class Message(AbstractModel):
    name = models.CharField(
        default='',
        max_length=255,
        verbose_name='Enter Your Name',
        blank=True,
    )
    email = models.EmailField(
        default='',
        max_length=255,
        verbose_name='Enter Email Address',

        blank=True,
    )
    subject = models.CharField(
        default='',
        max_length=255,
        verbose_name='Enter Subject',
        blank=True,
    )
    message = models.TextField(
        default='',
        max_length=999,
        verbose_name='Enter Message',
        blank=True,
    )
    def __str__(self):
        return f'Message: {self.name}'


    class Meta:
        verbose_name_plural = 'Messages'
        verbose_name = 'Message'
        ordering = ('-created_date',)

