from django.db import models

# Create your models here.

class Subscriber(models.Model):
    email = models.EmailField(unique=True, max_length=254)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email