# Generated by Django 2.2.1 on 2019-07-12 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20190711_1902'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='post',
            field=models.CharField(blank=True, default='DEFAULT VALUE', max_length=50),
        ),
    ]
