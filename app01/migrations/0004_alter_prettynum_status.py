# Generated by Django 4.1.7 on 2023-04-06 14:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_prettynum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='prettynum',
            name='status',
            field=models.SmallIntegerField(choices=[(1, '已占用'), (2, '未占用')], default=2, verbose_name='状态'),
        ),
    ]
