# Generated by Django 4.2.6 on 2023-10-06 04:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rank',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('surname', models.CharField(max_length=32)),
                ('name', models.CharField(max_length=32)),
                ('otch', models.CharField(max_length=32)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('utk', models.BooleanField(default=True)),
                ('duty', models.CharField(default='PDA', max_length=32)),
                ('job_title', models.CharField(blank=True, max_length=100)),
                ('rank', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='peoples.rank')),
            ],
        ),
    ]
