# Generated by Django 4.0.6 on 2022-11-05 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0016_alter_perfil_local'),
    ]

    operations = [
        migrations.AddField(
            model_name='perfil',
            name='data_nascimento',
            field=models.DateField(blank=True, null=True),
        ),
    ]