# Generated by Django 5.0.4 on 2024-05-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("svc", "0002_alter_vendor_vendor_code"),
    ]

    operations = [
        migrations.AlterField(
            model_name="purchaseorder",
            name="status",
            field=models.CharField(
                choices=[(0, "Pending"), (1, "Completed"), (2, "Cancelled")],
                default="pending",
                help_text="Current status of the PO",
            ),
        ),
    ]
