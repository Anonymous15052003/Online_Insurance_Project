# Generated by Django 5.0.6 on 2024-05-08 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('online_insurance', '0003_alter_agentavailability_lattitude_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='agentavailability',
            name='agent_district',
            field=models.CharField(choices=[('Ahmadnagar', 'Ahmadnagar'), ('Akola', 'Akola'), ('Amravati', 'Amravati'), ('Aurangabad', 'Aurangabad'), ('Bhandara', 'Bhandara'), ('Buldhana', 'Buldhana'), ('Chandrapur', 'Chandrapur'), ('Dhule', 'Dhule'), ('Gadchiroli', 'Gadchiroli'), ('Gondia', 'Gondia'), ('Hingoli', 'Hingoli'), ('Jalgaon', 'Jalgaon'), ('Jalna', 'Jalna'), ('Kolhapur', 'Kolhapur'), ('Latur', 'Latur'), ('MumbaiCity', 'Mumbai City'), ('MumbaiSuburban', 'Mumbai Suburban'), ('Nagpur', 'Nagpur'), ('Nanded', 'Nanded'), ('Nandurbar', 'Nandurbar'), ('Nashik', 'Nashik'), ('Osmanabad', 'Osmanabad'), ('Palghar', 'Palghar'), ('Parbhani', 'Parbhani'), ('Pune', 'Pune'), ('Raigad', 'Raigad'), ('Ratnagiri', 'Ratnagiri'), ('Sangli', 'Sangli'), ('Satara', 'Satara'), ('Sindhudurg', 'Sindhudurg'), ('Solapur', 'Solapur'), ('Thane', 'Thane'), ('Wardha', 'Wardha'), ('Washim', 'Washim'), ('Yavatmal', 'Yavatmal')], default='Mumbai Suburban', max_length=100),
            preserve_default=False,
        ),
    ]
