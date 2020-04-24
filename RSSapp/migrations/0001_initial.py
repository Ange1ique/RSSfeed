# Generated by Django 3.0.5 on 2020-04-23 17:07

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSS_URLS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.URLField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Feed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=128)),
                ('summary', models.CharField(blank=True, max_length=500)),
                ('published', models.DateField(blank=True, null=True)),
                ('updated', models.DateField(blank=True, null=True)),
                ('imported', models.DateField(default=datetime.date.today)),
                ('url', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='RSSapp.RSS_URLS')),
            ],
        ),
    ]