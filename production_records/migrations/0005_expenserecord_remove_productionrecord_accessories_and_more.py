# Generated by Django 4.2.7 on 2023-11-21 08:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('production_records', '0004_productionrecord_accessories_productionrecord_fabric_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExpenseRecord',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('fabric', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sewing', models.DecimalField(decimal_places=2, max_digits=10)),
                ('threads', models.DecimalField(decimal_places=2, max_digits=10)),
                ('accessories', models.DecimalField(decimal_places=2, max_digits=10)),
                ('other', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.RemoveField(
            model_name='productionrecord',
            name='accessories',
        ),
        migrations.RemoveField(
            model_name='productionrecord',
            name='fabric',
        ),
        migrations.RemoveField(
            model_name='productionrecord',
            name='other',
        ),
        migrations.RemoveField(
            model_name='productionrecord',
            name='sewing',
        ),
        migrations.RemoveField(
            model_name='productionrecord',
            name='threads',
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='model',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='received_by',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='productionrecord',
            name='total',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
    ]
