# Generated by Django 3.2.9 on 2021-11-29 17:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0007_alter_localuser_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='localuser',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='E-mail Address'),
        ),
    ]
