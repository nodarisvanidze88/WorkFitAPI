# Generated by Django 5.0.3 on 2024-03-09 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0003_alter_workouts_accessories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouts',
            name='workoutType',
            field=models.ManyToManyField(related_name='workoutTypes', to='workouts.workouttypes'),
        ),
    ]