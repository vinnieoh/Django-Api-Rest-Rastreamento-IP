# Generated by Django 4.0.2 on 2022-02-18 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_alter_ipmodel_zip'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipmodel',
            name='zip',
            field=models.DecimalField(decimal_places=10, default=0.0, max_digits=100, null=True),
        ),
    ]
