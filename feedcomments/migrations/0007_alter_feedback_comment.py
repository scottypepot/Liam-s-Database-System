# Generated by Django 5.1.1 on 2024-12-02 17:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feedcomments', '0006_alter_feedback_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='comment',
            field=models.TextField(),
        ),
    ]