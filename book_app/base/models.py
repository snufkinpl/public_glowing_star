from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class book(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
 
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100, default='')
    price = models.FloatField(max_length=10, default=39.99)
    description = models.TextField(null=True, blank=True)
    complete = models.BooleanField(default=False)
    borrow = models.BooleanField(default=False)
    # created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    class Meta:
        order_with_respect_to = 'user'
