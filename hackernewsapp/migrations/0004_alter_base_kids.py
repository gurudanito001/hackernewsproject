# Generated by Django 4.1.2 on 2022-10-27 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hackernewsapp', '0003_alter_base_kids'),
    ]

    operations = [
        migrations.AlterField(
            model_name='base',
            name='kids',
            field=models.CharField(default='', max_length=200),
        ),
    ]
