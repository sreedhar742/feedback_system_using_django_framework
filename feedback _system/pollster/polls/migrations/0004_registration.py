# Generated by Django 4.1.3 on 2023-12-08 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_student'),
    ]

    operations = [
        migrations.CreateModel(
            name='Registration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=100)),
                ('last_name', models.CharField(max_length=100)),
                ('id_name', models.CharField(max_length=100)),
                ('gmail', models.EmailField(max_length=254)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]