# Generated by Django 5.1.4 on 2024-12-31 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0017_comment_created_at_task_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='text',
            field=models.TextField(),
        ),
    ]
