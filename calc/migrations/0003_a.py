# Generated by Django 4.0.1 on 2022-02-02 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='a',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('open', models.FloatField(max_length=20)),
                ('high', models.FloatField(max_length=20)),
                ('low', models.FloatField(max_length=20)),
                ('close', models.FloatField(max_length=20)),
                ('adj_close', models.FloatField(max_length=20)),
                ('volume', models.IntegerField()),
                ('rsi', models.FloatField(max_length=20)),
                ('macd', models.TextField()),
                ('bollingerband_signal', models.TextField()),
            ],
        ),
    ]
