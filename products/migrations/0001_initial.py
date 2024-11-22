# Generated by Django 4.2 on 2024-11-22 11:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Название')),
                ('description', models.TextField(verbose_name='Описание')),
                ('price', models.PositiveIntegerField(verbose_name='Цена')),
                ('icon', models.ImageField(blank=True, null=True, upload_to='icon/', verbose_name='Иконка')),
                ('categories', models.CharField(blank=True, max_length=100, null=True, verbose_name='Категория')),
                ('available', models.BooleanField(default=True, verbose_name='Доступен')),
                ('rating', models.FloatField(default=0, verbose_name='Рейтинг')),
            ],
            options={
                'verbose_name': 'Продукт',
                'verbose_name_plural': 'Продукты',
            },
        ),
    ]
