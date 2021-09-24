# Generated by Django 3.2.7 on 2021-09-24 14:30

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('catalog', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False, unique=True)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('description', models.CharField(max_length=100)),
                ('transaction_date', models.DateTimeField()),
                ('user_note', models.CharField(default=None, max_length=100, null=True)),
                ('account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
                ('category', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='catalog.code')),
            ],
            options={
                'db_table': 'transactions',
                'managed': True,
            },
        ),
    ]
