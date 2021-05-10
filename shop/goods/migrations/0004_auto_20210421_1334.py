# Generated by Django 3.2 on 2021-04-21 09:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0003_rename_members_member'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='member',
            name='birth',
        ),
        migrations.RemoveField(
            model_name='member',
            name='name',
        ),
        migrations.AddField(
            model_name='member',
            name='address',
            field=models.TextField(max_length=10000, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='birth_date',
            field=models.DateTimeField(blank=True, help_text='Enter number of your birth', null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='email',
            field=models.EmailField(max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='firstname',
            field=models.CharField(default='', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='lastname',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='message',
            field=models.CharField(blank=True, max_length=400, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='phoneNumber',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='goods.product'),
        ),
        migrations.AddField(
            model_name='member',
            name='receivedmoney',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='member',
            name='zipCode',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='kodemeli',
            field=models.IntegerField(null=True),
        ),
    ]
