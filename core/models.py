from django.db import models

# Create your models here.


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField() 
    img = models.ImageField(upload_to="AboutUs_images", blank=True, null=True, verbose_name="Картинки 'О нас'")

    class Meta:
        verbose_name = "О нас"
        verbose_name_plural = "О нас"


class TeamCodifyLab(models.Model):
    name = models.CharField(max_length=255)
    descriptions = models.TextField()
    img_team = models.ImageField(upload_to="TeamsImg", blank=True, null=True, verbose_name="Картинки команды CodifyLab")

    class Meta:
        verbose_name = "Команда CodifyLab"
        verbose_name_plural = "Команды CodifyLab"



class ContanctsCodifyLab(models.Model):
    name = models.CharField(max_length=255)
    mail = models.CharField(max_length=200)
    phone_number = models.CharField(max_length=20)
    whatsapp_number = models.CharField(max_length=20)
    instagram = models.CharField(max_length=55)
    twitter = models.CharField(max_length=55)
    facebook = models.CharField(max_length=55)

    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"


class Plus(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    img_plus = models.ImageField(upload_to="Plus_img", blank=True, null=True, verbose_name="Картинки Plus")

    class Meta:
        verbose_name = "Преимущество"
        verbose_name_plural = "Преимущества"


class Franchise(models.Model):
    name = models.CharField(max_length=250)
    text = models.TextField()
    img_franchise = models.ImageField(upload_to="Franchise_img", blank=True, null=True, verbose_name="Картинки франишизы")

    class Meta:
        verbose_name = "Франшиза"
        verbose_name_plural = "Франшизы"


class Application(models.Model):
    name = models.CharField(max_length=250)
    message = models.TextField()
    mail = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Форма отправки"
        verbose_name_plural = "Форма отправки"


class Feedback(models.Model):
    name = models.CharField(max_length=250)
    img_feedback = models.ImageField(upload_to="Feedbacks_img", null=True, blank=True, verbose_name="Картинки отзывов)")
    message = models.TextField()
    mail = models.EmailField(max_length=254)
    phone_number = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"

