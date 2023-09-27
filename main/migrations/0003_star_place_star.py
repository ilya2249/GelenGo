# Generated by Django 4.2.4 on 2023-08-30 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_typeplace_place_distance_place_price_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Star',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название')),
                ('code', models.CharField(max_length=255, verbose_name='Код')),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='star',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='main.star'),
        ),
    ]
