# Generated by Django 3.0.8 on 2020-08-04 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_newsstory_image_link'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsstory',
            name='image_link',
            field=models.URLField(default='', max_length=500),
        ),
    ]
