# Generated by Django 4.1.7 on 2023-04-12 15:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('riders', '0001_initial'),
        ('orders', '0008_alter_orderdetails_rider'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderdetails',
            name='rider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='riders.rider'),
        ),
    ]