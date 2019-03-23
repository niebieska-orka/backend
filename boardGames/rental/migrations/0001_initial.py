# Generated by Django 2.1.7 on 2019-03-23 12:19

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Game',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=550)),
                ('picture_url', models.CharField(max_length=150)),
                ('publisher', models.CharField(max_length=100)),
                ('score', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('surname', models.CharField(max_length=100)),
                ('mail', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reservation_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('borrow_date', models.DateTimeField()),
                ('borrower', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Person')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.Game')),
            ],
        ),
    ]