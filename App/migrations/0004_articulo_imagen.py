# Generated by Django 4.0.5 on 2022-07-29 03:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_articulo'),
    ]

    operations = [
        migrations.AddField(
            model_name='articulo',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='articulos'),
        ),
    ]