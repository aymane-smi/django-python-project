# Generated by Django 2.2.16 on 2021-05-31 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Parc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom_parc', models.CharField(blank=True, max_length=400)),
                ('nbr_machine', models.IntegerField(default=0)),
                ('nbr_err', models.IntegerField(default=0)),
                ('demande_s', models.BooleanField(default=False)),
                ('nbr_ram', models.IntegerField(default=0)),
                ('nbr_dd', models.IntegerField(default=0)),
                ('nbr_os', models.IntegerField(default=0)),
                ('nbr_af', models.IntegerField(default=0)),
                ('adresse', models.CharField(blank=True, max_length=400)),
                ('nbr_autre', models.IntegerField(default=0)),
                ('alt', models.FloatField(default=0)),
                ('long', models.FloatField(default=0)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='admin', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
