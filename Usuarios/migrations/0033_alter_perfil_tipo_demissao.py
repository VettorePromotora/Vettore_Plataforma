# Generated by Django 4.0.6 on 2022-12-07 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Usuarios', '0032_perfil_email_p'),
    ]

    operations = [
        migrations.AlterField(
            model_name='perfil',
            name='tipo_demissao',
            field=models.CharField(blank=True, choices=[('Sem justa causa', 'Sem justa causa'), ('Com justa causa', 'Com justa causa'), ('Pedido de demissão', 'Pedido de demissão'), ('Acordo', 'Acordo'), ('consensual', 'consensual')], max_length=18, null=True, verbose_name='Tipo de Demissão'),
        ),
    ]
