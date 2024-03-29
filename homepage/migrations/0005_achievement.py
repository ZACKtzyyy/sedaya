# Generated by Django 4.2.2 on 2023-07-01 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0004_delete_achievement'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achname', models.CharField(max_length=100)),
                ('achdesc', models.TextField()),
                ('achvenue', models.CharField(max_length=100)),
                ('achdate', models.DateField()),
                ('achstanding', models.IntegerField()),
                ('achcategory', models.CharField(max_length=50)),
            ],
        ),
    ]
