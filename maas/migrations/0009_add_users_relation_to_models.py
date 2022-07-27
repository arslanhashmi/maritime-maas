# Generated by Django 3.2.2 on 2022-07-04 11:28

from django.conf import settings
from django.db import migrations, models


def migrate_users(apps, schema_editor):
    OperatorModal = apps.get_model('maas', 'MaasOperator')
    for row in OperatorModal.objects.all():
        row.users.add(row.user)


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('maas', '0008_add_availability_api_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='maasoperator',
            name='users',
            field=models.ManyToManyField(related_name='maas_operators', to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
        migrations.AddField(
            model_name='ticketingsystem',
            name='users',
            field=models.ManyToManyField(related_name='ts_users', to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
        migrations.AddField(
            model_name='transportserviceprovider',
            name='users',
            field=models.ManyToManyField(related_name='tsp_users', to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
        migrations.RunPython(migrate_users, migrations.RunPython.noop),
    ]
