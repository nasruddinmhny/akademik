# Generated by Django 5.0.3 on 2024-06-14 02:19

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("perkuliahan", "0001_initial"),
    ]

    operations = [
        migrations.DeleteModel(
            name="cikgu",
        ),
        migrations.DeleteModel(
            name="guru",
        ),
    ]