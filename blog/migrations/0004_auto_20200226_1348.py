# Generated by Django 3.0.2 on 2020-02-26 08:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['created_date']},
        ),
    ]
