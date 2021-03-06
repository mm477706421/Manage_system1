# Generated by Django 3.1.2 on 2020-10-27 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserAgent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=16)),
                ('passwd', models.CharField(max_length=16)),
                ('reg_date_time', models.DateTimeField(auto_now_add=True)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
            options={
                'ordering': ['reg_date_time'],
            },
        ),
    ]
