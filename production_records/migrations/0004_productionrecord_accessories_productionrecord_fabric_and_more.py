# Generated by Django 4.2.7 on 2023-11-21 07:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_records', '0003_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='productionrecord',
            name='accessories',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productionrecord',
            name='fabric',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productionrecord',
            name='other',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productionrecord',
            name='sewing',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='productionrecord',
            name='threads',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='model',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='price',
            field=models.FloatField(),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='received_by',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='total',
            field=models.FloatField(default=0.0),
        ),
    ]
