# Generated by Django 5.1 on 2024-09-29 14:20

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('anote_ai', '0003_anotacao_data_anotacao_status_anotacao_titulo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anotacao',
            name='data',
            field=models.DateField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='anotacao',
            name='titulo',
            field=models.TextField(max_length=255),
        ),
    ]
