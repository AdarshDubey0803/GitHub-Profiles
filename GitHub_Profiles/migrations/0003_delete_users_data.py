# Generated by Django 3.2.7 on 2021-09-19 15:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('GitHub_Profiles', '0002_rename_users_users_data'),
    ]

    operations = [
        migrations.DeleteModel(
            name='users_data',
        ),
    ]
