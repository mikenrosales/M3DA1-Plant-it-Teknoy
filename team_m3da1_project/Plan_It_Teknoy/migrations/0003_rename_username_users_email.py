# Generated by Django 3.2.6 on 2022-09-03 04:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Plan_It_Teknoy', '0002_auto_20220903_1155'),
    ]

    operations = [
        migrations.RenameField(
            model_name='users',
            old_name='username',
            new_name='email',
        ),
    ]
