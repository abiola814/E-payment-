# Generated by Django 3.1.7 on 2021-03-17 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='email',
            field=models.EmailField(default='otiboatengjoe@gmail.com', max_length=254),
            preserve_default=False,
        ),
    ]
