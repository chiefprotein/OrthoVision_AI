# Generated by Django 5.0 on 2024-04-18 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("myapp", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="xrayimages",
            name="img",
            field=models.ImageField(upload_to="Xrayimages/"),
        ),
    ]
