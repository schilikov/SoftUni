# Generated by Django 4.0.3 on 2022-03-15 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_pet_unique_together'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='pet',
            name='type',
            field=models.CharField(choices=[('Cat', 'Cat'), ('Dog', 'Dog'), ('Bunny', 'Bunny'), ('Parrot', 'Parrot'), ('Fish', 'Fish'), ('Other', 'Other')], max_length=6),
        ),
    ]
