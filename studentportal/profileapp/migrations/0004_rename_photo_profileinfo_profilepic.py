# Generated by Django 4.0.3 on 2022-04-14 10:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profileapp', '0003_profileinfo_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profileinfo',
            old_name='photo',
            new_name='profilepic',
        ),
    ]
