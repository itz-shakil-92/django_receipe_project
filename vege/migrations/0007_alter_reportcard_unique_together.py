# Generated by Django 4.2.7 on 2024-06-07 22:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('vege', '0006_reportcard'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='reportcard',
            unique_together={('student_rank', 'date_of_report_card_generation')},
        ),
    ]
