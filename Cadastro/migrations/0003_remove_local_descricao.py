# Generated by Django 4.0.6 on 2022-08-09 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0002_alter_local_descricao_alter_local_nome'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='local',
            name='descricao',
        ),
    ]
