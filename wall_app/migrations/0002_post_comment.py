# Generated by Django 3.1.2 on 2020-10-14 22:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wall_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='comment',
            field=models.ManyToManyField(related_name='comments', to='wall_app.User'),
        ),
    ]