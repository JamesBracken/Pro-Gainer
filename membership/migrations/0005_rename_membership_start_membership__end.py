# Generated by Django 5.2.2 on 2025-06-17 21:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('membership', '0004_rename_next_payment_date_membership_membership_end_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='membership_start',
            new_name='_end',
        ),
    ]
