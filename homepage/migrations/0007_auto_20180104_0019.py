# Generated by Django 2.0 on 2018-01-03 22:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20180103_1909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='image',
            field=models.FileField(default='static/images/no-img.png', upload_to='uploads/'),
        ),
    ]
