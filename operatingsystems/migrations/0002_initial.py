# Generated by Django 3.2.19 on 2023-12-11 22:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('operatingsystems', '0001_initial'),
        ('repos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='osgroup',
            name='repos',
            field=models.ManyToManyField(blank=True, to='repos.Repository'),
        ),
        migrations.AddField(
            model_name='os',
            name='osgroup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='operatingsystems.osgroup'),
        ),
    ]
