# Generated by Django 3.2 on 2021-04-25 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0014_auto_20210425_1118'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='ProductSize',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(related_name='products', to='goods.Image'),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ManyToManyField(related_name='products', to='goods.Category'),
        ),
    ]
