# Generated by Django 4.0.4 on 2022-05-27 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('email', models.EmailField(max_length=64)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=64)),
            ],
        ),
    ]
