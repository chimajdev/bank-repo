# Generated by Django 2.0.2 on 2018-07-04 22:22

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
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_type', models.CharField(choices=[('SA', 'Savings Account'), ('CA', 'Current Account'), ('JA', 'Joint Account')], max_length=2)),
                ('account_number', models.CharField(max_length=13, unique=True)),
                ('account_balance', models.DecimalField(decimal_places=2, max_digits=18)),
                ('last_deposit', models.DecimalField(decimal_places=2, max_digits=10)),
                ('interest_rate', models.DecimalField(decimal_places=0, max_digits=3)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='accounts', to=settings.AUTH_USER_MODEL, verbose_name='The related user')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_account', models.CharField(max_length=13)),
                ('to_account', models.CharField(max_length=13)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
                ('date_created', models.DateField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
