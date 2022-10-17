from distutils.command.upload import upload
from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Portifolio(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to = "static/images/")
    category = models.ForeignKey("portifolio.Category", on_delete=models.CASCADE)
    langauges = models.CharField(max_length=255)
    description = models.TextField()
    link = models.CharField(max_length=50)
    
    def __str__(self) -> str:
        return self.name

class Email(models.Model):
    contact_name = models.CharField(max_length=50)
    contact_email = models.EmailField(max_length=254)
    subject = models.CharField(max_length=50)
    message = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.contact_name
    