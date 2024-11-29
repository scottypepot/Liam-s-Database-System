from django.db import models

class Branch(models.Model):
    name = models.CharField(max_length=100, default = 'Liams')
    location = models.CharField(max_length=255)
    image = models.ImageField(upload_to='branch_images/', null=True, blank=True)  # Add image field

    def __str__(self):
        return self.name
