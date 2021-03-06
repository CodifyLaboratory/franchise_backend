# Generated by Django 3.2.2 on 2021-05-08 14:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_faq'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='aboutus',
            options={'verbose_name': 'О нас', 'verbose_name_plural': 'О нас'},
        ),
        migrations.AlterModelOptions(
            name='application',
            options={'verbose_name': 'Форма отправки', 'verbose_name_plural': 'Форма отправки'},
        ),
        migrations.AlterModelOptions(
            name='contanctscodifylab',
            options={'verbose_name': 'Контакт', 'verbose_name_plural': 'Контакты'},
        ),
        migrations.AlterModelOptions(
            name='faq',
            options={'verbose_name': 'Вопрос', 'verbose_name_plural': 'Вопросы'},
        ),
        migrations.AlterModelOptions(
            name='feedback',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
        migrations.AlterModelOptions(
            name='franchise',
            options={'verbose_name': 'Франшиза', 'verbose_name_plural': 'Франшизы'},
        ),
        migrations.AlterModelOptions(
            name='plus',
            options={'verbose_name': 'Преимущество', 'verbose_name_plural': 'Преимущества'},
        ),
        migrations.AlterModelOptions(
            name='teamcodifylab',
            options={'verbose_name': 'Команда CodifyLab', 'verbose_name_plural': 'Команды CodifyLab'},
        ),
    ]
