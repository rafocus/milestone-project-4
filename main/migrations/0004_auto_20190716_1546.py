# Generated by Django 2.2.3 on 2019-07-16 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20190716_1524'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[('PN', 'Pending'), ('IP', 'In progress'), ('CT', 'Completed')], default='PN', max_length=100),
        ),
        migrations.AlterField(
            model_name='ticket',
            name='ticket_type',
            field=models.CharField(choices=[('BG', 'Bug'), ('FT', 'Feature')], default='BG', max_length=100),
        ),
    ]
