# Generated by Django 2.2.5 on 2020-07-11 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('faq', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='general_questions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.CharField(max_length=300)),
                ('answer', models.TextField()),
                ('tag', models.CharField(choices=[('eng', 'eng'), ('ar', 'ar')], default='eng', max_length=5)),
            ],
        ),
    ]