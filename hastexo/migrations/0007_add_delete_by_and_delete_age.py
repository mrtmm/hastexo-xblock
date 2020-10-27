# Generated by Django 2.2.16 on 2020-11-04 13:35

from django.db import migrations, models
import hastexo.models


class Migration(migrations.Migration):

    dependencies = [
        ('hastexo', '0006_auto_20200107_1332'),
    ]

    operations = [
        migrations.AddField(
            model_name='stack',
            name='delete_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stack',
            name='delete_by',
            field=models.DateTimeField(db_index=True, default=hastexo.models.default_delete_by_timestamp, null=True),  # noqa E501
        ),
        migrations.AddField(
            model_name='stacklog',
            name='delete_age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='stacklog',
            name='delete_by',
            field=models.DateTimeField(db_index=True, default=hastexo.models.default_delete_by_timestamp, null=True),  # noqa E501
        ),
    ]
