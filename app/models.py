from django.db import models
from django.core.validators import validate_email


class Email(models.Model):
    destination = models.CharField(max_length=120, blank=False, validators=[validate_email])
    letter_subject = models.CharField(max_length=256, blank=True)
    message = models.TextField(blank=True)
    created_document_timestamp = models.DateTimeField(auto_now_add=True, blank=True)

    class Meta:
        db_table = 'Email'
