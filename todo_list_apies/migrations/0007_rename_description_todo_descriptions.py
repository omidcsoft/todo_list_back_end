# Generated by Django 4.1 on 2022-08-21 14:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('todo_list_apies', '0006_todo_token'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='description',
            new_name='descriptions',
        ),
    ]
