# Generated by Django 5.1.8 on 2025-04-09 08:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('palace', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['name'], 'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['name'], 'verbose_name': 'услуга', 'verbose_name_plural': 'услуги'},
        ),
    ]
