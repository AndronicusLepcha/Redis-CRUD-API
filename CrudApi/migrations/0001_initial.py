# Generated by Django 4.2.10 on 2024-07-22 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='dummy_model_data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(blank=True, max_length=20)),
                ('created_by', models.CharField(blank=True, max_length=20)),
                ('file_type', models.CharField(blank=True, max_length=20)),
                ('file_size', models.IntegerField(null=True)),
                ('file', models.FileField(upload_to='uploads/')),
                ('description', models.TextField(blank=True, null=True)),
                ('is_public', models.BooleanField(default=False)),
                ('file_extension', models.CharField(blank=True, max_length=10)),
                ('tags', models.CharField(blank=True, max_length=100)),
                ('is_archived', models.BooleanField(default=False)),
                ('category', models.CharField(blank=True, max_length=50)),
            ],
        ),
    ]
