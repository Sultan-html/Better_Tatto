# Generated by Django 5.1.3 on 2025-01-01 16:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_contacts'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=40, verbose_name='Адресс')),
                ('Phone', models.CharField(max_length=40, verbose_name='Номер телефона')),
                ('Fax', models.CharField(max_length=40, verbose_name='Номер телефона')),
                ('Mail', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('facebook', models.URLField(verbose_name='Ссылка на facebook')),
                ('twitter', models.URLField(verbose_name='Ссылка на twitter')),
                ('pinterest', models.URLField(verbose_name='Ссылка на pinterest')),
                ('youtube', models.URLField(verbose_name='Ссылка на youtube')),
            ],
            options={
                'verbose_name': 'Связь',
                'verbose_name_plural': 'Связи',
            },
        ),
    ]