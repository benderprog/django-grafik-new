# Generated by Django 4.2.6 on 2023-10-06 05:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('peoples', '0002_duty_remove_person_duty'),
    ]

    operations = [
        migrations.AddField(
            model_name='person',
            name='duty',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='peoples.duty'),
        ),
    ]