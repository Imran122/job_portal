# Generated by Django 3.2.6 on 2021-08-12 17:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0004_auto_20210812_1715'),
    ]

    operations = [
        migrations.AddField(
            model_name='job',
            name='expiredate',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='job',
            name='categories',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='jobs.categorey'),
        ),
    ]
