# Generated by Django 2.2 on 2020-12-20 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gameapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='frames',
            name='frame10_bonus',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame10_first',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame10_second',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame3_first',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame3_second',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame4_first',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame4_second',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame5_first',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame5_second',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame6_first',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame6_second',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame7_first',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame7_second',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame8_first',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame8_second',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame9_first',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='frames',
            name='frame9_second',
            field=models.CharField(blank=True, default=0, max_length=10, null=True),
        ),
    ]
