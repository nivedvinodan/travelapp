# Generated by Django 4.1.3 on 2022-12-12 09:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('studyapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('names', models.CharField(max_length=250)),
                ('imgs', models.ImageField(upload_to='pics')),
                ('descs', models.TextField()),
            ],
        ),
    ]
