# Generated by Django 3.2.17 on 2023-02-15 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCA', '0007_report1'),
    ]

    operations = [
        migrations.AddField(
            model_name='report1',
            name='dt',
            field=models.CharField(default=0, max_length=60),
        ),
    ]
