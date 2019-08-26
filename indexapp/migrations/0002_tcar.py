# Generated by Django 2.0.6 on 2019-07-30 01:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('indexapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tcar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('book_name', models.CharField(blank=True, max_length=20, null=True)),
                ('book_num', models.CharField(blank=True, max_length=20, null=True)),
                ('user_name', models.CharField(blank=True, max_length=20, null=True)),
            ],
            options={
                'managed': False,
                'db_table': 't_car',
            },
        ),
    ]
