# Generated by Django 4.2.1 on 2023-06-23 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('new_app', '0006_remove_post_likes_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/static/images/default.png', upload_to='static/images'),
        ),
    ]
