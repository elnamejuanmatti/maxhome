# Generated by Django 5.0.6 on 2024-10-23 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Productos',
            fields=[
                ('Codigo', models.AutoField(primary_key=True, serialize=False)),
                ('Nombre', models.TextField(max_length=50)),
                ('Cantidad', models.TextField(max_length=15)),
                ('Ubicacion', models.TextField(max_length=20)),
                ('Imagen', models.ImageField(null=True, upload_to='Personajes')),
            ],
        ),
    ]