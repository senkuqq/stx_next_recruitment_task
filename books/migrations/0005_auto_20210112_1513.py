# Generated by Django 3.1.5 on 2021-01-12 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_auto_20210112_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='authors',
            field=models.ManyToManyField(blank=True, null=True, to='books.Author'),
        ),
        migrations.AlterField(
            model_name='book',
            name='average_rating',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='published_date',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='ratings_count',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
