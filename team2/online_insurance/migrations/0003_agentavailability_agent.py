# Generated by Django 5.0.4 on 2024-05-08 14:06

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("online_insurance", "0002_agentavailability"),
    ]

    operations = [
        migrations.AddField(
            model_name="agentavailability",
            name="agent",
            field=models.CharField(default="Default Agent", max_length=100),
        ),
    ]
