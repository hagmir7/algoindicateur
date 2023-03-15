from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify
from django.utils.crypto import get_random_string



class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True)
    avatar = models.ImageField(upload_to='avatar/', default='user_default.webp', blank=True)
    phone = models.IntegerField(blank=True, default=False)
    country = models.CharField(max_length=40, blank=True)
    blocked = models.BooleanField(default=False, blank=True)
    update = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    last_visit = models.DateTimeField(auto_now=True)
    verificated = models.BooleanField(default=False)
    slug = models.SlugField(blank=True, null=True)
    

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name} - {self.created.strftime('%d-%m-%Y')}"

    
    def save(self, *args, **kwargs):
        self.slug = slugify(str(self.user.username))
        return super().save(*args, **kwargs)
    
    def get_absolute_url(self):
        return f'/{self.slug}'



