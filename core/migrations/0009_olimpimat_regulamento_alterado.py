# Generated by Django 3.2.2 on 2021-06-14 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0008_auto_20210614_1358"),
    ]

    operations = [
        migrations.AddField(
            model_name="olimpimat",
            name="regulamento_alterado",
            field=models.FileField(default="", upload_to="regulamento/%Y/%m/%d/"),
            preserve_default=False,
        ),
    ]
