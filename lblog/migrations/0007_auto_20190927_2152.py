# Generated by Django 2.2.5 on 2019-09-27 21:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lblog', '0006_auto_20190927_1613'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blogpost',
            options={'ordering': ['-published_date', '-updated', '-timestamp']},
        ),
    ]
