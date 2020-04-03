# Generated by Django 2.2.6 on 2020-04-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_init_data'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temperaturen',
            name='temperatur',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterUniqueTogether(
            name='sensors',
            unique_together={('adresse', 'serverschrank')},
        ),
    ]
