# Generated by Django 5.0.1 on 2024-01-07 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainpage', '0003_rename_category_name_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='img_src',
            field=models.ImageField(blank=True, default=None, null=True, upload_to='mainpage/static/mainpage/'),
        ),
    ]
