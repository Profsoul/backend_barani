# Generated by Django 3.1.7 on 2021-04-06 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('marketing', '0002_auto_20210406_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer_detail',
            name='CIN_no',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='customer_detail',
            name='GST_no',
            field=models.CharField(default=None, max_length=30, null=True),
        ),
    ]