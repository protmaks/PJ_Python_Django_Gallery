# Generated by Django 4.1.4 on 2022-12-24 09:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import gallery.models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('gallery', '0005_country_remove_image_geo_location_image_geo_location'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='peoples_names',
        ),
        migrations.AddField(
            model_name='image',
            name='peoples',
            field=models.ManyToManyField(blank=True, null=True, related_name='peoples', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='author', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='picture',
            field=models.ImageField(default='default_gallery.jpg', upload_to=gallery.models.user_directory_path),
        ),
    ]
