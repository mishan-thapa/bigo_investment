# Generated by Django 4.0.1 on 2022-02-03 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('calc', '0004_technical'),
    ]

    operations = [
        migrations.CreateModel(
            name='technical1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('companies', models.TextField()),
                ('rsi', models.FloatField(max_length=20)),
                ('macd', models.TextField()),
                ('bollingerband', models.TextField()),
            ],
        ),
        migrations.DeleteModel(
            name='technical',
        ),
    ]