# Generated by Django 4.1.3 on 2022-12-18 11:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coworking', '0013_remove_location_time_create_cities_content_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='cities',
            options={'verbose_name': 'Города Беларуси', 'verbose_name_plural': 'Города Беларуси'},
        ),
        migrations.AlterField(
            model_name='location',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coworking.cities', verbose_name='Города'),
        ),
        migrations.AlterField(
            model_name='location',
            name='num',
            field=models.CharField(max_length=255, verbose_name='Номер улицы'),
        ),
        migrations.CreateModel(
            name='Addpage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Коворкинга')),
                ('street', models.CharField(max_length=255, verbose_name='Улица')),
                ('num', models.CharField(max_length=255, verbose_name='Номер улицы')),
                ('number', models.CharField(max_length=255, verbose_name='Контактный номер')),
                ('content', models.TextField(blank=True, verbose_name='Описание')),
                ('time_update', models.DateTimeField(auto_now=True, verbose_name='Время изменения')),
                ('cat', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='coworking.cities', verbose_name='Города')),
            ],
            options={
                'verbose_name': 'Статьи пользователя',
                'verbose_name_plural': 'Статьи пользователя',
                'ordering': ['time_update'],
            },
        ),
    ]
