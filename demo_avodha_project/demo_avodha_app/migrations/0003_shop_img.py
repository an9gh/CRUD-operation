# Generated by Django 4.0.5 on 2022-06-13 06:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_avodha_app', '0002_rename_pric_shop_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='shop',
            name='img',
            field=models.ImageField(default='0', upload_to='images'),
            preserve_default=False,
        ),
    ]