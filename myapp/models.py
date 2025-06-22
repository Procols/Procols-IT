from django.db import models

class ContactInfo(models.Model):  
    email = models.EmailField()
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.email
