# Generated by Django 5.0.1 on 2024-01-06 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='category_id',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='game',
            name='category_id',
            field=models.IntegerField(),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]