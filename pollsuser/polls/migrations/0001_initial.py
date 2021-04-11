# Generated by Django 2.2.10 on 2021-04-10 07:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('poll_id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(default='', max_length=255, unique=True, verbose_name='Заголовок')),
                ('date_start', models.DateTimeField(auto_now_add=True, verbose_name='Старт опроса')),
                ('date_end', models.DateTimeField(auto_now=True, verbose_name='Конец опроса')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание опроса')),
            ],
            options={
                'ordering': ['-poll_id'],
            },
        ),
    ]