# Generated by Django 3.2.5 on 2021-12-03 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materias',
            name='url_image',
            field=models.URLField(),
        ),
    ]
