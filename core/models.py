from django.db import models

# Create your models here.


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField() 
    img = models.ImageField(upload_to="AboutUs_images", blank=True, null=True, verbose_name="Картинки 'О нас'")


class TeamCodifyLab(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    img_team = models.ImageField(upload_to="TeamsImg", blank=True, null=True, verbose_name="Картинки команды CodifyLab")



class ContanctsCodifyLab(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    instagram = models.CharField(max_length=55)
    twitter = models.CharField(max_length=55)
    facebook = models.CharField(max_length=55)


class Plus(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img_plus = models.ImageField(upload_to="Plus_img", blank=True, null=True, verbose_name="Картинки Plus")
    