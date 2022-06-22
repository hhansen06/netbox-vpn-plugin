# Generated by Django 4.0.5 on 2022-06-21 10:03

import django.core.serializers.json
from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('tenancy', '0007_contact_link'),
        ('extras', '0073_journalentry_tags_custom_fields'),
    ]

    operations = [
        migrations.CreateModel(
            name='Vpn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('last_updated', models.DateTimeField(auto_now=True, null=True)),
                ('custom_field_data', models.JSONField(blank=True, default=dict, encoder=django.core.serializers.json.DjangoJSONEncoder)),
                ('gegenstelle', models.CharField(max_length=100)),
                ('comments', models.TextField(blank=True)),
                ('customer_contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='tenancy.contact')),
                ('tags', taggit.managers.TaggableManager(through='extras.TaggedItem', to='extras.Tag')),
                ('tenant', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='tenancy.tenant')),
            ],
            options={
                'ordering': ('gegenstelle',),
            },
        ),
    ]
