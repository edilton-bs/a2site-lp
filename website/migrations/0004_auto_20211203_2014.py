# Generated by Django 3.2.5 on 2021-12-03 23:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_usuario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='usuario',
            old_name='com_materia',
            new_name='comb_materia',
        ),
        migrations.AlterField(
            model_name='usuario',
            name='idade',
            field=models.IntegerField(),
        ),
    ]