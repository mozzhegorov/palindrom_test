# Generated by Django 4.1.3 on 2022-11-06 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0002_alter_track_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='composer',
            name='title',
            field=models.CharField(help_text='Composer title', max_length=150, unique=True, verbose_name='title'),
        ),
    ]
