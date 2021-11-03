# Generated by Django 3.2.4 on 2021-06-28 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DragonAge', '0003_auto_20210628_1127'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='companion',
        ),
        migrations.AddField(
            model_name='companion',
            name='game',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DragonAge.game'),
        ),
    ]