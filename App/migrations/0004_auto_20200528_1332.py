# Generated by Django 2.2.6 on 2020-05-28 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_auto_20200403_0935'),
    ]

    operations = [
        migrations.AlterField(
            model_name='benutzer',
            name='password',
            field=models.CharField(max_length=256),
        ),
    ]
