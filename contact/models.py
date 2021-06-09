from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=200,null=True)
    patient_id = models.CharField(max_length=100,null=True)
    age = models.PositiveIntegerField()
    phone_number = models.CharField(max_length=300,null=True)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ['date_updated']
        verbose_name = "Register"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.name}"