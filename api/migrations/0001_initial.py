# Generated by Django 5.1.1 on 2024-10-08 22:15

import django.db.models.deletion
import tinymce.models
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ContractProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract_project', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Contract Projects',
                'ordering': ('-created_at',),
            },
        ),
        migrations.CreateModel(
            name='Contract',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', tinymce.models.HTMLField(blank=True, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='due created')),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tasks', to=settings.AUTH_USER_MODEL)),
                ('contract_project', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='contract', to='api.contractproject')),
            ],
            options={
                'verbose_name_plural': 'Contracts',
                'ordering': ('-created_at',),
            },
        ),
    ]
