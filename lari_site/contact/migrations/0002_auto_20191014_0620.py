# Generated by Django 2.2.5 on 2019-10-14 13:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contact', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact_arabic',
            new_name='contact_info',
        ),
        migrations.DeleteModel(
            name='contact_english',
        ),
    ]
