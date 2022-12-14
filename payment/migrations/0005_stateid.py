# Generated by Django 4.0 on 2022-10-11 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0004_payment_state_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='StateID',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('address', models.CharField(max_length=200)),
                ('identity', models.CharField(max_length=200)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
