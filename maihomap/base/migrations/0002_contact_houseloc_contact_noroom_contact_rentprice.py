# Generated by Django 4.1.4 on 2023-06-16 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='houseloc',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='noroom',
            field=models.IntegerField(default=5),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='rentprice',
            field=models.IntegerField(default=5000),
            preserve_default=False,
        ),
    ]