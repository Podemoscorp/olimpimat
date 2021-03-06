# Generated by Django 3.2.2 on 2021-06-07 10:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("core", "0005_alter_challenge_url_prova"),
    ]

    operations = [
        migrations.AddField(
            model_name="new",
            name="abstract",
            field=models.TextField(
                default="", help_text="news summary", verbose_name="Abstract"
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="new",
            name="image",
            field=models.ImageField(
                blank=True,
                help_text="news cover image",
                upload_to="%Y/%m/%d/",
                verbose_name="Imagem",
            ),
        ),
        migrations.AddField(
            model_name="new",
            name="processed_abstract",
            field=models.TextField(
                blank=True,
                default="",
                help_text="news processed summary",
                verbose_name="processed Abstract",
            ),
        ),
        migrations.AddField(
            model_name="new",
            name="processed_content",
            field=models.TextField(
                blank=True,
                default="",
                help_text="news processed content",
                verbose_name="Processed Content",
            ),
        ),
        migrations.AddField(
            model_name="new",
            name="views",
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name="new",
            name="content",
            field=models.TextField(help_text="news content", verbose_name="Content"),
        ),
        migrations.AlterField(
            model_name="new",
            name="posted_in",
            field=models.DateTimeField(
                blank=True,
                default=django.utils.timezone.now,
                help_text="news posting date",
                verbose_name="Posted in",
            ),
        ),
        migrations.AlterField(
            model_name="new",
            name="poster",
            field=models.ForeignKey(
                help_text="news editor",
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="new",
            name="title",
            field=models.CharField(
                help_text="title of the news", max_length=100, verbose_name="Title"
            ),
        ),
    ]
