# Generated by Django 5.1.1 on 2024-11-29 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('branch', '0004_remove_branch_created_at_remove_branch_created_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='branch',
            name='name',
            field=models.CharField(default='Liams', max_length=100),
        ),
    ]
