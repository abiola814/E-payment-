# Generated by Django 4.0 on 2022-10-09 23:12

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_payment_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='fee_type',
            field=models.CharField(default=10, max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='payment',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='payment',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
