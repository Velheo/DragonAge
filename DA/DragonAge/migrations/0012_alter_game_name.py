# Generated by Django 3.2.4 on 2021-09-20 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DragonAge', '0011_alter_game_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
