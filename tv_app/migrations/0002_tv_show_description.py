# Generated by Django 2.2.4 on 2020-10-10 23:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tv_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tv_show',
            name='description',
            field=models.CharField(default='The TV Show', max_length=255),
            preserve_default=False,
        ),
    ]