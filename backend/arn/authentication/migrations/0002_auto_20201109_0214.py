# Generated by Django 3.1.3 on 2020-11-09 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='arnuser',
            name='updated',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
