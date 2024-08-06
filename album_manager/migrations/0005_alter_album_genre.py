# Generated by Django 4.2 on 2024-08-05 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album_manager', '0004_alter_album_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='genre',
            field=models.CharField(choices=[('R', 'Rock'), ('C', 'Clasica'), ('B', 'Bossa Nova'), ('E', 'Electronica'), ('H', 'Hip-Hop')], max_length=30),
        ),
    ]