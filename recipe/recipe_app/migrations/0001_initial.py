# Generated by Django 5.1.7 on 2025-03-20 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Recipe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Name of the recipe', max_length=255)),
                ('ingredients', models.TextField(help_text='Comma-separated ingredients for the recipe')),
                ('instructions', models.TextField(help_text='Cooking instructions for the recipe')),
                ('cooking_time', models.PositiveIntegerField(help_text='Time in minutes')),
                ('image', models.ImageField(blank=True, null=True, upload_to='recipe_images/')),
            ],
        ),
    ]
