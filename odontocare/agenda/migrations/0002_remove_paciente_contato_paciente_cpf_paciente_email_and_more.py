# Generated by Django 5.1.1 on 2024-10-05 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='paciente',
            name='contato',
        ),
        migrations.AddField(
            model_name='paciente',
            name='cpf',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='paciente',
            name='telefone',
            field=models.CharField(blank=True, max_length=11, null=True),
        ),
    ]
