# Generated by Django 3.1.2 on 2021-01-04 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0012_auto_20201117_2344'),
    ]

    operations = [
        migrations.AddField(
            model_name='classc3',
            name='section',
            field=models.IntegerField(default=3, verbose_name='section'),
            preserve_default=False,
        ),
    ]