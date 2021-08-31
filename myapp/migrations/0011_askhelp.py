# Generated by Django 3.1.2 on 2020-11-17 17:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0010_delete_askhelp'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameField', models.CharField(max_length=300)),
                ('roll', models.IntegerField()),
                ('objectlost', models.CharField(max_length=300)),
                ('desribe', models.TextField()),
                ('contactdetails', models.CharField(max_length=10)),
                ('post_date', models.DateField()),
            ],
        ),
    ]