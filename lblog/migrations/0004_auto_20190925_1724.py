# Generated by Django 2.2.5 on 2019-09-25 17:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lblog', '0003_auto_20190919_2248'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='title',
            field=models.CharField(max_length=120),
        ),
    ]