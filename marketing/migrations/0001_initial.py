# Generated by Django 3.1.2 on 2020-12-18 09:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer_Detail',
            fields=[
                ('Customer_id', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('Email_id', models.EmailField(max_length=254)),
                ('Customer_name', models.CharField(max_length=50)),
                ('Nick_name', models.CharField(max_length=30)),
                ('Address', models.TextField()),
                ('GST_no', models.CharField(max_length=30)),
                ('CIN_no', models.CharField(max_length=30)),
                ('Contact_1', models.CharField(max_length=10)),
                ('Contact_2', models.CharField(max_length=10)),
                ('Contact_3', models.CharField(max_length=10)),
                ('Contact_4', models.CharField(max_length=10)),
            ],
        ),
    ]