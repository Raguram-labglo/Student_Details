# Generated by Django 4.1.2 on 2022-10-17 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('details', '0008_remove_mark_mail'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='mail',
            field=models.CharField(max_length=30, null=True),
        ),
    ]