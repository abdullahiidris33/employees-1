# Generated by Django 5.1.4 on 2024-12-22 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0008_remove_employee_email_remove_employee_first_name_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='default@example.com', max_length=355, unique=True),
        ),
        migrations.AddField(
            model_name='employee',
            name='first_name',
            field=models.CharField(default='Abdullahi', max_length=25),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='employee',
            name='last_name',
            field=models.CharField(default='idris', max_length=25),
            preserve_default=False,
        ),
    ]
