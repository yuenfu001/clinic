from django.db import models

# Create your models here.
class Contact(models.Model):
    SEX = (
        ("MALE", "Male"),
        ("FEMALE", "Female"),
    )

    full_name = models.CharField(
        max_length=200,
        null=True,
        help_text="Enter your First name, middle name then last name",
    )
    card_ID = models.CharField(max_length=100, null=True)
    age = models.PositiveIntegerField()
    sex = models.CharField(max_length=7, choices=SEX, blank=True)
    tel = models.CharField(max_length=300, null=True)
    address = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True, auto_now=False)
    date_updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        ordering = ["-date_updated"]
        verbose_name = "Register"
        verbose_name_plural = "Contacts"

    def __str__(self):
        return f"{self.full_name}"
