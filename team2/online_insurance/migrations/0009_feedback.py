# Generated by Django 5.0.4 on 2024-05-24 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_insurance', '0008_alter_agentavailability_agent_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('contact', models.CharField(max_length=15)),
                ('feedback', models.TextField()),
            ],
        ),
    ]