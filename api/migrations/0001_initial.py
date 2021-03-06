# Generated by Django 3.2.4 on 2021-07-02 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserCrud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=100)),
                ('date_of_birth', models.DateField(max_length=20)),
                ('profession', models.CharField(max_length=30)),
            ],
        ),
    ]
