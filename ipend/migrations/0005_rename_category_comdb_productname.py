# Generated by Django 4.1.3 on 2023-01-14 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipend', '0004_alter_comdb_price_alter_prodb_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comdb',
            old_name='category',
            new_name='productname',
        ),
    ]
