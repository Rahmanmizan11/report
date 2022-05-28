# Generated by Django 3.2.5 on 2022-01-26 05:57

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
            name='UserDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_no', models.CharField(max_length=20, null=True)),
                ('address', models.TextField(max_length=100, null=True)),
                ('gender', models.CharField(max_length=10, null=True)),
                ('dob', models.DateField(blank=True, null=True)),
                ('is_seller', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('has_applied', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
