# Generated by Django 3.1.2 on 2020-11-17 15:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_form_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='AskHelp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300)),
                ('roll', models.IntegerField(verbose_name='Roll number')),
                ('objectlost', models.CharField(max_length=300)),
                ('contactdet', models.CharField(max_length=10)),
                ('description', models.TextField()),
                ('pub_date', models.DateField()),
            ],
        ),
        migrations.AlterField(
            model_name='form',
            name='contact',
            field=models.CharField(max_length=10, verbose_name='Contact No'),
        ),
    ]
