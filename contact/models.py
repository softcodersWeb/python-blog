from django.db import models

# Create your models here.
class Contacts(models.Model):
    name = models.CharField(max_length=110)
    subject = models.CharField(max_length=110)
    
    email = models.EmailField(max_length=254)
    message = models.TextField(max_length=1000)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email