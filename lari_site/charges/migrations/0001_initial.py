# Generated by Django 2.2.5 on 2020-05-09 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='charges_headline',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('headline', models.CharField(max_length=100)),
                ('table_headline', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='charges_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.CharField(max_length=200)),
                ('tag', models.CharField(choices=[('eng', 'eng'), ('ar', 'ar')], default='eng', max_length=5)),
                ('Headline', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='charges.charges_headline')),
            ],
        ),
    ]
