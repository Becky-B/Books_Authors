# Generated by Django 2.2 on 2020-03-11 21:14

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('books_authorsApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='authors',
            name='notes',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
