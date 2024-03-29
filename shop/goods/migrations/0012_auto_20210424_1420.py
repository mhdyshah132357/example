# Generated by Django 3.2 on 2021-04-24 09:50

from django.db import migrations, models
import versatileimagefield.fields


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0011_auto_20210424_1229'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('image', versatileimagefield.fields.VersatileImageField(upload_to='images/', verbose_name='Image')),
                ('image_ppoi', versatileimagefield.fields.PPOIField(default='0.5x0.5', editable=False, max_length=20)),
            ],
        ),
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['-created']},
        ),
        migrations.AddField(
            model_name='product',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateField(auto_now=True, null=True),
        ),
        migrations.AlterField(
            model_name='member',
            name='status',
            field=models.CharField(blank=True, choices=[('green', 'Green'), ('yellow', 'Yellow'), ('red', 'Red'), ('gray', 'Gray')], default='y', help_text='enter the  status by colors', max_length=10),
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ManyToManyField(related_name='products', to='goods.Image'),
        ),
    ]
