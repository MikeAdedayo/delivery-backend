# Generated by Django 2.1.2 on 2019-04-04 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cafe', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cafete',
            name='food_type',
            field=models.CharField(default='Rice', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='cafete',
            name='food_image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]