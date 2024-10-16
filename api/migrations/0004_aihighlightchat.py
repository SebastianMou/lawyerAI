# Generated by Django 5.1.1 on 2024-10-13 23:11

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_contractproject_description_and_more'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AIHighlightChat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('highlighted_text', models.TextField()),
                ('instruction', models.TextField()),
                ('ai_response', models.TextField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('contract_project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ai_chats', to='api.contractproject')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'AI Highlight Chats',
                'ordering': ('-created_at',),
            },
        ),
    ]
