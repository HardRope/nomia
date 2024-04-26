# Generated by Django 4.1.9 on 2024-04-26 02:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CateringType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True, verbose_name='тип')),
            ],
            options={
                'verbose_name': 'заведение',
                'verbose_name_plural': 'заведения',
            },
        ),
        migrations.CreateModel(
            name='Result',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='данные опроса')),
                ('catering_type', models.ManyToManyField(related_name='results', to='quiz_app.cateringtype')),
                ('patricipiant', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='results', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'результат опроса',
                'verbose_name_plural': 'результаты опросов',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='вопрос')),
                ('multiple', models.BooleanField(default=False)),
                ('catering', models.ManyToManyField(blank=True, null=True, related_name='questions', to='quiz_app.cateringtype')),
            ],
            options={
                'verbose_name': 'вопрос',
                'verbose_name_plural': 'вопросы',
            },
        ),
        migrations.CreateModel(
            name='Option',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.CharField(max_length=255, verbose_name='ответ')),
                ('catering', models.ManyToManyField(blank=True, null=True, related_name='options', to='quiz_app.cateringtype')),
                ('question', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='options', to='quiz_app.question')),
            ],
            options={
                'verbose_name': 'ответ',
                'verbose_name_plural': 'ответы',
            },
        ),
    ]
