# Generated by Django 4.1.4 on 2022-12-18 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_rename_image_image_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='geo_location',
            field=models.CharField(blank=True, max_length=120, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='peoples_names',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
