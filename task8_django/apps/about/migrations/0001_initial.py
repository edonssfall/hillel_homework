# Generated by Django 4.0.6 on 2022-07-08 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Whoami',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_agent', models.CharField(max_length=255)),
                ('ip_adress', models.CharField(max_length=255)),
                ('now_time', models.CharField(max_length=255)),
            ],
        ),
    ]
