# Generated by Django 5.1.2 on 2024-10-12 12:54

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='age',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Возраст')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Возраст',
                'verbose_name_plural': 'Возрасты',
            },
        ),
        migrations.CreateModel(
            name='chislo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='НАПИШИТЕ КОЛИЧЕСТВО ЧЕЛОВЕК')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
            ],
            options={
                'verbose_name': 'Количество',
                'verbose_name_plural': 'Количеств',
            },
        ),
        migrations.CreateModel(
            name='slozhno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название cложности')),
                ('description', models.TextField(default='Описание отсутствует', verbose_name='Описание соһложности')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Сложность',
                'verbose_name_plural': 'Сложности',
            },
        ),
        migrations.CreateModel(
            name='strashno',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название cложностьи')),
                ('description', models.TextField(default='Описание отсутствует', verbose_name='Описание страшности')),
                ('slug', models.SlugField(blank=True, editable=False, unique=True)),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время создания')),
            ],
            options={
                'verbose_name': 'Страшность',
                'verbose_name_plural': 'Страшности',
            },
        ),
        migrations.CreateModel(
            name='Quest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название квеста')),
                ('description', models.TextField(default='Описание отсутствует', verbose_name='Описание квеста')),
                ('created_at', models.DateTimeField(default=datetime.datetime.now, verbose_name='Время создания')),
                ('age', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startit_app.age', verbose_name='Выберите возраст')),
                ('slozhno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startit_app.slozhno', verbose_name='Выберите cложность')),
                ('strashno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='startit_app.strashno', verbose_name='Выберите страшность')),
            ],
            options={
                'verbose_name': 'Квест',
                'verbose_name_plural': 'Квесты',
            },
        ),
    ]