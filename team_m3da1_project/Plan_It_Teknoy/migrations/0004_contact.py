# Generated by Django 4.0.3 on 2022-09-03 09:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Plan_It_Teknoy', '0003_rename_username_users_email'),
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Not set', max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('message', models.CharField(max_length=250)),
            ],
        ),
    ]
