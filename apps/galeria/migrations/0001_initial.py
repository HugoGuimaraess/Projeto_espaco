# Generated by Django 4.2.3 on 2023-07-21 00:44

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Fotografia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('legenda', models.CharField(max_length=150)),
                ('descricao', models.TextField()),
                ('foto', models.ImageField(blank=True, upload_to='Fotos/%Y/%m/%d/')),
                ('publicada', models.BooleanField(default=False)),
                ('categoria', models.CharField(choices=[('NEBULOSA', 'nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100)),
                ('data', models.DateTimeField(default=datetime.datetime.now)),
                ('tipo', models.CharField(choices=[('NEBULOSA', 'nebulosa'), ('ESTRELA', 'Estrela'), ('GALAXIA', 'Galáxia'), ('PLANETA', 'Planeta')], default='', max_length=100)),
            ],
        ),
    ]