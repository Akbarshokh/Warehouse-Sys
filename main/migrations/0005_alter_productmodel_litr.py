# Generated by Django 4.0.5 on 2022-06-15 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_milkmodel_litr_alter_productmodel_litr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productmodel',
            name='litr',
            field=models.FloatField(default=0),
        ),
    ]
