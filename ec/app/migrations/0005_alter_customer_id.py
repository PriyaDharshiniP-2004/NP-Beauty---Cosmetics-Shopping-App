# Generated by Django 3.2 on 2024-10-17 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_alter_customer_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='id',
            field=models.CharField(default='67114b1446b97e90976ed76d', editable=False, max_length=24, primary_key=True, serialize=False),
        ),
    ]