# Generated by Django 3.2.2 on 2021-05-08 14:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_application'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('img_feedback', models.ImageField(blank=True, null=True, upload_to='Feedbacks_img', verbose_name='Картинки отзывов)')),
                ('message', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
    ]