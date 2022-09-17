# Generated by Django 4.0.6 on 2022-07-16 13:29

import django.contrib.postgres.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=255, null=True, verbose_name='IMDB Id')),
                ('title_type', models.CharField(choices=[('short', 'Short'), ('movie', 'Movie')], max_length=255, null=True, verbose_name='Title Type')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('is_adult', models.BooleanField(default=False, verbose_name='Is Adult')),
                ('year', models.DateField(default='0', verbose_name='Year')),
                ('genres', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None, verbose_name='Genre')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imdb_id', models.CharField(max_length=255, null=True, verbose_name='IMDB Id')),
                ('name', models.CharField(max_length=255, null=True, verbose_name='Name')),
                ('birth_year', models.DateField(default='0', verbose_name='Birth Year')),
                ('death_year', models.DateField(default='0', verbose_name='Death Year')),
            ],
        ),
        migrations.CreateModel(
            name='PersonMovie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order', models.IntegerField(null=True, verbose_name='Order')),
                ('category', models.CharField(max_length=255, null=True, verbose_name='Category')),
                ('job', models.CharField(max_length=255, null=True, verbose_name='Job')),
                ('characters', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), null=True, size=None, verbose_name='Characters')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movie.movie')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='movie.person')),
            ],
        ),
    ]