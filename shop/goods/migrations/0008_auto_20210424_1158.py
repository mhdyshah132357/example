# Generated by Django 3.2 on 2021-04-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0007_member_status'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='member',
            options={'ordering': ['check']},
        ),
        migrations.AddField(
            model_name='member',
            name='check',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(blank=True, choices=[('a', 'Activate'), ('s', 'Staff status'), ('u', 'Supperuser status')], default='a', help_text='enter the accessibility', max_length=10),
        ),
    ]
