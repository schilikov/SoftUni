# Generated by Django 4.0.3 on 2022-03-11 13:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employees', '0003_employee_egn_alter_employee_last_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='job_title',
            field=models.IntegerField(choices=[(1, 'Software Developer'), (2, 'QA Engineer'), (3, 'DevOps Specialist')], default=1),
            preserve_default=False,
        ),
    ]
