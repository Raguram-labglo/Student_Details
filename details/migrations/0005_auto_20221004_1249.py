# Generated by Django 3.2.15 on 2022-10-04 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0004_alter_mark_updated_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='mark',
            name='created_by',
            field=models.CharField(max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='mark',
            name='updated_by',
            field=models.CharField(max_length=20, null=True),
        ),
    ]