# Generated by Django 3.2.14 on 2022-08-25 11:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pictures', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operator',
            name='picture',
        ),
    ]