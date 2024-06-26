# Generated by Django 5.0.4 on 2024-05-30 17:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("online_insurance", "0010_merge_0009_feedback_0009_userprofile"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="appointment",
            name="time_from",
        ),
        migrations.RemoveField(
            model_name="appointment",
            name="time_to",
        ),
        migrations.AddField(
            model_name="agentavailability",
            name="time_slots",
            field=models.CharField(
                default="", max_length=300, verbose_name="Time Slots"
            ),
        ),
        migrations.AddField(
            model_name="appointment",
            name="date",
            field=models.DateField(default=datetime.date.today),
        ),
        migrations.AddField(
            model_name="appointment",
            name="time_slots",
            field=models.CharField(
                choices=[
                    ("1-2", "1-2"),
                    ("2-3", "2-3"),
                    ("3-4", "3-4"),
                    ("4-5", "4-5"),
                    ("5-6", "5-6"),
                    ("6-7", "6-7"),
                    ("7-8", "7-8"),
                    ("8-9", "8-9"),
                    ("9-10", "9-10"),
                    ("10-11", "10-11"),
                    ("11-12", "11-12"),
                    ("12-13", "12-13"),
                    ("13-14", "13-14"),
                    ("14-15", "14-15"),
                    ("15-16", "15-16"),
                    ("16-17", "16-17"),
                    ("17-18", "17-18"),
                    ("18-19", "18-19"),
                    ("19-20", "19-20"),
                    ("20-21", "20-21"),
                    ("21-22", "21-22"),
                    ("22-23", "22-23"),
                    ("23-24", "23-24"),
                ],
                default="",
                max_length=300,
                verbose_name="Time Slots",
            ),
        ),
    ]
