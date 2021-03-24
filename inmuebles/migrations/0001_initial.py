# Generated by Django 3.0 on 2021-03-23 15:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigo', models.CharField(max_length=100)),
                ('tipo', models.CharField(max_length=50)),
                ('ubicacion', models.CharField(max_length=1000)),
                ('edo', models.CharField(blank=True, max_length=1000)),
                ('precio', models.DecimalField(decimal_places=2, max_digits=7)),
                ('description', models.TextField()),
                ('image', models.FileField(blank=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='InmuebleImage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(upload_to='images/')),
                ('inmueble', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='inmuebles.Inmueble')),
            ],
        ),
    ]