# Generated by Django 3.2.5 on 2021-07-05 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='fav_products',
            field=models.ManyToManyField(blank=True, to='app.Product'),
        ),
    ]
