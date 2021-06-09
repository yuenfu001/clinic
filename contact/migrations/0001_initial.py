# Generated by Django 3.2.4 on 2021-06-08 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, null=True)),
                ('patient_id', models.CharField(max_length=100, null=True)),
                ('age', models.PositiveIntegerField()),
                ('phone_number', models.CharField(max_length=300, null=True)),
                ('address', models.TextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
            options={
                'verbose_name': 'Register',
                'verbose_name_plural': 'Contacts',
                'ordering': ['date_updated'],
            },
        ),
    ]