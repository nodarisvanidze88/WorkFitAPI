# Generated by Django 5.0.3 on 2024-03-09 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('workouts', '0002_alter_accessories_accessories_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='workouts',
            name='accessories',
            field=models.ManyToManyField(blank=True, to='workouts.accessories'),
        ),
    ]