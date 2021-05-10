# Generated by Django 3.2 on 2021-04-24 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0006_remove_member_product'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Activate'), ('s', 'Staff status'), ('u', 'Supperuser status')], default='a', max_length=10),
        ),
    ]
