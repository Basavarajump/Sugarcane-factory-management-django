# Generated by Django 3.2.3 on 2023-01-30 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MCA', '0005_admin1'),
    ]

    operations = [
        migrations.CreateModel(
            name='report',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sugar', models.CharField(max_length=60)),
                ('molass', models.CharField(max_length=60)),
                ('filt', models.CharField(max_length=60)),
                ('baga', models.CharField(max_length=60)),
                ('straw', models.CharField(max_length=60)),
                ('tops', models.CharField(max_length=60)),
                ('total', models.CharField(max_length=60)),
            ],
        ),
    ]