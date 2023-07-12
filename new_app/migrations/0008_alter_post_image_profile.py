# Generated by Django 4.2.1 on 2023-07-05 16:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('new_app', '0007_post_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='/media/images/default.png', upload_to='./'),
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('publish_time', models.DateTimeField(auto_now_add=True)),
                ('edit_time', models.DateTimeField(auto_now=True)),
                ('username', models.CharField(max_length=140)),
                ('email', models.EmailField(max_length=254)),
                ('avatar', models.ImageField(default='/media/images/avatars/default.png', upload_to='./')),
                ('bio', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]