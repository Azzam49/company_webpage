# Generated by Django 5.0 on 2024-01-17 14:26

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0010_blog_author"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog", name="content", field=ckeditor.fields.RichTextField(),
        ),
    ]