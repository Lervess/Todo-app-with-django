# Generated by Django 4.2.1 on 2023-06-05 15:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0002_tag'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='tag',
            field=models.ManyToManyField(to='todo.tag'),
        ),
    ]
