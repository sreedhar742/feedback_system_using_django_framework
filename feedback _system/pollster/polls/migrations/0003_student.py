# Generated by Django 4.1.3 on 2023-12-07 16:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0002_sir_alter_question_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student', models.CharField(max_length=50, verbose_name='enter your name')),
                ('father', models.CharField(max_length=50, verbose_name='enter your father name')),
                ('mother', models.CharField(max_length=50, verbose_name='enter your father name')),
            ],
        ),
    ]
