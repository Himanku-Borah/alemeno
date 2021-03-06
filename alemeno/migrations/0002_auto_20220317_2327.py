# Generated by Django 3.2.9 on 2022-03-17 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('alemeno', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='approved_by',
            field=models.ForeignKey(blank=True, editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='image',
            name='created_on',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
