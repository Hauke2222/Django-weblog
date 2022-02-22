# Generated by Django 4.0.2 on 2022-02-13 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('date', models.DateField(auto_now_add=True)),
                ('author', models.CharField(max_length=250)),
                ('text', models.TextField()),
            ],
        ),
    ]