# Generated by Django 4.2.10 on 2024-05-15 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hastexo', '0012_add_suspend_by'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='connection_id',
            field=models.CharField(blank=True, max_length=128, null=True),
        ),
    ]
