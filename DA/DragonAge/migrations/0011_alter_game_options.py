# Generated by Django 3.2.4 on 2021-09-20 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DragonAge', '0010_classes_img'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='game',
            options={'ordering': ['name']},
        ),
    ]
