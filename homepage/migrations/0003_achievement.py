# Generated by Django 4.2.2 on 2023-06-28 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Achievement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('achievementdesc', models.TextField()),
                ('achievementcategory', models.CharField(max_length=100)),
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='homepage.image')),
            ],
        ),
    ]
