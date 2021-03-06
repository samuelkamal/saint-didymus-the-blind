# Generated by Django 3.2.7 on 2021-09-26 02:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Img_1', models.ImageField(upload_to='media/')),
                ('Title_1', models.CharField(max_length=200)),
                ('Description_1', models.TextField()),
                ('Img_2', models.ImageField(upload_to='media/')),
                ('Title_2', models.CharField(max_length=200)),
                ('Description_2', models.TextField()),
                ('Img_3', models.ImageField(upload_to='media/')),
                ('Title_3', models.CharField(max_length=200)),
                ('Description_3', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Magazin_Number',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(max_length=150)),
                ('Description', models.TextField()),
                ('DownLoad_Link', models.CharField(max_length=1000)),
            ],
        ),
    ]
