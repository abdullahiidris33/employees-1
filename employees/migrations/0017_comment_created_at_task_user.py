# Generated by Django 5.1.4 on 2024-12-31 08:31

# import django.db.models.deletion
# from django.conf import settings
# from django.db import migrations, models


# class Migration(migrations.Migration):

#     dependencies = [
#         ('employees', '0016_remove_comment_author_remove_comment_created_at_and_more'),
#         migrations.swappable_dependency(settings.AUTH_USER_MODEL),
#     ]

#     operations = [
#         migrations.AddField(
#             model_name='comment',
#             name='created_at',
#             field=models.DateTimeField(auto_now_add=True, default=1),
#             preserve_default=False,
#         ),
#         migrations.AddField(
#             model_name='task',
#             name='user',
#             field=models.ForeignKey(default='user', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
#             preserve_default=False,
#         ),
#     ]

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0016_remove_comment_author_remove_comment_created_at_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime.now),  # Use a callable for default
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='task',
            name='user',
            field=models.ForeignKey(
                default=1,  # Replace with an actual valid user ID in your database
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
            preserve_default=False,
        ),
    ]
