from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Profile model to store user balance and other custom fields
class Balance(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)  # Link to the User model
    amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Store user balance

    def __str__(self):
        return f'{self.user.username} - Balance: {self.amount}'