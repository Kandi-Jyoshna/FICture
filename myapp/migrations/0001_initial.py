# Generated by Django 3.1.2 on 2020-11-12 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClassC3',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rollno', models.IntegerField(verbose_name='Roll No')),
                ('name', models.CharField(max_length=300)),
            ],
        ),
    ]
