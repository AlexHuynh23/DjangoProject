# Generated by Django 3.1.6 on 2021-06-08 06:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='date_created',
            new_name='pubDate',
        ),
        migrations.RemoveField(
            model_name='post',
            name='type',
        ),
        migrations.AlterField(
            model_name='post',
            name='likes',
            field=models.IntegerField(default=0),
        ),
    ]
