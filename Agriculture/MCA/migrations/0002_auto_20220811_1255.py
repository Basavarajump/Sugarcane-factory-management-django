# Generated by Django 3.2.13 on 2022-08-11 07:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('MCA', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='register1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(max_length=60)),
                ('password', models.CharField(max_length=60)),
                ('phno', models.CharField(max_length=60)),
                ('adharno', models.CharField(max_length=60)),
                ('Image', models.CharField(max_length=60)),
            ],
        ),
        migrations.AlterField(
            model_name='issue',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MCA.register1'),
        ),
    ]
