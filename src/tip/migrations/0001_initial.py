# Generated by Django 4.0 on 2022-05-24 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tip',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=60)),
                ('description', models.TextField(null=True)),
                ('metadata', models.JSONField(null=True)),
            ],
            options={
                'db_table': 'tips',
                'managed': True,
            },
        ),
    ]
