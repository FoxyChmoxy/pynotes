# Generated by Django 2.2.6 on 2019-10-21 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Login', models.CharField(max_length=10, verbose_name='Логин')),
                ('Password', models.CharField(max_length=20, verbose_name='Пароль')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Text', models.CharField(max_length=255, verbose_name='Заметка')),
                ('User', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='notes.User')),
            ],
        ),
    ]
