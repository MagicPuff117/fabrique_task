# Generated by Django 4.0.3 on 2022-03-27 15:25

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.PositiveIntegerField(validators=[django.core.validators.RegexValidator(message='номер телефона клиента в формате 7XXXXXXXXXX (X - цифра от 0 до 9)', regex='^7\\w{10}$')], verbose_name='Мобильный телефон')),
                ('code', models.PositiveIntegerField(verbose_name='Код мобильного оператора')),
                ('tag', models.CharField(blank=True, max_length=50, verbose_name='Тэги для поиска')),
                ('time_zone', models.CharField(max_length=10, verbose_name='Часовой пояс')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beginning', models.DateTimeField(verbose_name='Начало рассылки')),
                ('ending', models.DateTimeField(verbose_name='Окончание рассылки')),
                ('text', models.TextField(verbose_name='Текст сообщения')),
                ('mobile_codes', models.CharField(blank=True, max_length=50, verbose_name='Коды мобильных операторов')),
                ('tags', models.CharField(blank=True, max_length=50, verbose_name='Тэги для поиска')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='Дата отправки')),
                ('status', models.CharField(choices=[('sent', 'Sent'), ('proceeded', 'Proceeded'), ('failed', 'Failed')], max_length=15, verbose_name='Статус отправки')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='service.client')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='service.mailing')),
            ],
            options={
                'verbose_name': 'Сообщение',
                'verbose_name_plural': 'Сообщения',
            },
        ),
    ]
