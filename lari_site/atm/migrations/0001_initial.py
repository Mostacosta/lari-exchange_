# Generated by Django 2.2.5 on 2019-11-26 16:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('branches', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='atm_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adress_name', models.CharField(max_length=100)),
                ('adress_details', models.CharField(max_length=300)),
                ('map', models.CharField(max_length=500)),
                ('tag', models.CharField(choices=[('eng', 'eng'), ('ar', 'ar')], default='eng', max_length=5)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='branches.branch_master')),
            ],
        ),
    ]
