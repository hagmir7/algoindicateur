from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone



class Category(models.Model):
    name = models.CharField(max_length=300)

    def __str__(self):
        return self.name

class Language(models.Model):
    language = models.CharField(("Langue"), max_length=50)
    code = models.CharField(("Code"), max_length=50)

    def __str__(self):
        return self.language



class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(("Title"), max_length=200)
    image = models.ImageField(upload_to='postImage')
    description = models.TextField()
    body = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)



    def __str__(self):
        return self.title
    

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=300)
    image = models.ImageField(upload_to='images')
    price = models.IntegerField(default=0)
    old_price = models.IntegerField(null=True, blank=True)
    cart = models.ManyToManyField(User, blank=True, related_name="user_cart")
    description = models.TextField()
    body = models.TextField()
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    slug = models.SlugField(null=True, blank=True)
    code = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return self.name



class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    message = models.TextField()
    phone = models.CharField(default='', max_length=30)
    is_read = models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return self.email
    


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    full_name = models.CharField(max_length=300, blank=True, null=True)
    email = models.EmailField(max_length=300, blank=True, null=True)
    phone = models.CharField(max_length=20, blank=True, null=True)
    products = models.ManyToManyField(Product, related_name='product_order')
    payment = models.CharField(max_length=100)
    confirmed = models.BooleanField(default=False)
    canceled = models.BooleanField(default=False)
    is_payed = models.BooleanField(default=False)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True,blank=True, null=True)




class Benefit(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=500)
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True, blank=True)


    def __str__(self):
        return self.title


