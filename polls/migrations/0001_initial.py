# Generated by Django 4.2.7 on 2023-12-04 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('BookTitle', models.CharField(max_length=50)),
                ('BookAuthor', models.CharField(max_length=30)),
                ('BookId', models.IntegerField()),
            ],
        ),
    ]
