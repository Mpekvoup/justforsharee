# Generated by Django 5.1.2 on 2024-10-15 16:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('startit_app', '0008_remove_addresesq_contacts_addresesq_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='addresesq',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2024, 10, 15, 16, 36, 48, 642248, tzinfo=datetime.timezone.utc)),
            preserve_default=False,
        ),
    ]
