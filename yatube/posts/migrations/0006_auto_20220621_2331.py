# Generated by Django 2.2.19 on 2022-06-21 20:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_auto_20220621_2227'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='description',
            field=models.TextField(verbose_name='description of the group'),
        ),
    ]
