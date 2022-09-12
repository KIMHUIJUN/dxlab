# Generated by Django 3.2.14 on 2022-08-26 07:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email')),
                ('date_of_birth', models.DateField()),
                ('sex', models.TextField()),
                ('want_field_front', models.BooleanField()),
                ('want_field_back', models.BooleanField()),
                ('want_field_data', models.BooleanField()),
                ('want_field_ai', models.BooleanField()),
                ('front_level', models.IntegerField()),
                ('back_level', models.IntegerField()),
                ('data_level', models.IntegerField()),
                ('ai_level', models.IntegerField()),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
