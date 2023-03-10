# Generated by Django 4.0.6 on 2022-10-15 17:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Cadastro', '0013_alter_solicitacao_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Auxiliar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('local_produto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cadastro.local')),
                ('produto_detalhes', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cadastro.produtos')),
                ('produto_solicitacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cadastro.solicitacao')),
                ('produto_status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Cadastro.status')),
            ],
        ),
    ]
