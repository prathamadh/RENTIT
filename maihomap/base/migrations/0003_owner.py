# Generated by Django 4.1.4 on 2023-06-16 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_contact_houseloc_contact_noroom_contact_rentprice'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('houseloc', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=70)),
                ('phone', models.CharField(max_length=12)),
                ('desc', models.CharField(max_length=500)),
                ('rentprice', models.IntegerField()),
                ('noroom', models.IntegerField()),
            ],
        ),
    ]
