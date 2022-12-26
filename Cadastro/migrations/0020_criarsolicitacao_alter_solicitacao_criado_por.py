# Generated by Django 4.0.6 on 2022-10-21 22:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Cadastro', '0019_alter_produtos_estoque_atl'),
    ]

    operations = [
        migrations.CreateModel(
            name='CriarSolicitacao',
            fields=[
            ],
            options={
                'verbose_name': 'solicitando material',
                'proxy': True,
                'indexes': [],
                'constraints': [],
            },
            bases=('Cadastro.solicitacao',),
        ),
        migrations.AlterField(
            model_name='solicitacao',
            name='criado_por',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]