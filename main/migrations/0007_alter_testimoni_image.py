# Generated by Django 3.2.9 on 2022-08-20 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_testimoni_estado'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testimoni',
            name='image',
            field=models.ImageField(default=1, upload_to='testimonios'),
            preserve_default=False,
        ),
    ]
