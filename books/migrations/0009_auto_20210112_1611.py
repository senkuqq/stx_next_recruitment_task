# Generated by Django 3.1.5 on 2021-01-12 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0008_auto_20210112_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='ratings_count',
            field=models.IntegerField(blank=True, max_length=20, null=True),
        ),
    ]
