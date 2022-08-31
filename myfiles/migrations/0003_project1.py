# Generated by Django 4.0.4 on 2022-08-13 03:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myfiles', '0002_project'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nomi', models.CharField(max_length=40)),
                ('malumot', models.TextField()),
                ('rasm', models.ImageField(upload_to='media')),
                ('vaqt', models.DateTimeField(auto_now=True)),
                ('tur', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myfiles.type')),
            ],
        ),
    ]
