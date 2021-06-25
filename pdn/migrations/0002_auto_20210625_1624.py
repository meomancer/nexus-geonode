# Generated by Django 3.2.4 on 2021-06-25 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pdn', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='alert',
            name='remote_id',
            field=models.BigIntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='expert',
            name='remote_id',
            field=models.BigIntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='news',
            name='remote_id',
            field=models.BigIntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='remote_id',
            field=models.BigIntegerField(default=0, unique=True),
            preserve_default=False,
        ),
    ]
