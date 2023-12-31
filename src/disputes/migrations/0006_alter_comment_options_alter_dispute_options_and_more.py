# Generated by Django 4.1 on 2023-11-27 06:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('disputes', '0005_filecomment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_at'], 'verbose_name': 'Комментарий', 'verbose_name_plural': 'Комментарии'},
        ),
        migrations.AlterModelOptions(
            name='dispute',
            options={'ordering': ['-created_at'], 'verbose_name': 'Спор', 'verbose_name_plural': 'Споры'},
        ),
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(25), django.core.validators.RegexValidator(message='Текст может быть только на латинице и кириллице', regex='^[A-Za-zА-Яа-я0-9ёЁ\\s\\W]+$')], verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='dispute',
            name='description',
            field=models.TextField(max_length=1000, validators=[django.core.validators.MinLengthValidator(25), django.core.validators.RegexValidator(message='Текст может быть только на латинице и кириллице', regex='^[A-Za-zА-Яа-я0-9ёЁ\\s\\W]+$')], verbose_name='Описание'),
        ),
    ]
