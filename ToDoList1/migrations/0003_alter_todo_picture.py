# Generated by Django 4.2.1 on 2023-11-25 15:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ToDoList1', '0002_todo_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todo',
            name='picture',
            field=models.ImageField(blank=True, default='https://images.app.goo.gl/BJcJytaDin7V3Zw49', null=True, upload_to='img'),
        ),
    ]
