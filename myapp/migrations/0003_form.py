# Generated by Django 3.1.2 on 2020-11-16 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_faculty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Form',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('objectname', models.CharField(max_length=300)),
                ('place', models.CharField(max_length=300)),
            ],
        ),
    ]