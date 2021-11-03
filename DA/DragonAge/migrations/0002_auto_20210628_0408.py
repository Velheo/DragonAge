# Generated by Django 3.2.4 on 2021-06-28 01:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('DragonAge', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Companion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imy', models.CharField(blank=True, max_length=20, null=True)),
                ('img', models.ImageField(blank=True, null=True, upload_to='Companion/')),
                ('classes', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DragonAge.classes')),
                ('race', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DragonAge.race')),
            ],
        ),
        migrations.AddField(
            model_name='game',
            name='companion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='DragonAge.companion'),
        ),
    ]
