# Generated by Django 4.1.9 on 2024-04-26 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz_app', '0002_result'),
    ]

    operations = [
        migrations.AddField(
            model_name='result',
            name='catering_type',
            field=models.ManyToManyField(related_name='results', to='quiz_app.cateringtype'),
        ),
    ]