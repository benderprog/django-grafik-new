# Generated by Django 4.2.6 on 2023-10-06 05:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Duty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
                ('description', models.TextField(max_length=100)),
            ],
        ),
        migrations.RemoveField(
            model_name='person',
            name='duty',
        ),
    ]
