from django.db import models


# Create your models here.
class Subscription(models.Model):
    email = models.EmailField(unique=True)
    stripe_customer_id = models.CharField(max_length=100, unique=True)
    stripe_subscription_id = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.email
