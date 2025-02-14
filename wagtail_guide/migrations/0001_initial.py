# Generated by Django 2.1.8 on 2019-05-18 11:38

import django.db.models.deletion
from django.db import migrations, models
from wagtail import VERSION as WAGTAIL_VERSION

if WAGTAIL_VERSION >= (3, 0):
    import wagtail.blocks as wagtail_blocks
    import wagtail.fields as wagtail_fields
else:
    import wagtail.core.blocks as wagtail_blocks
    import wagtail.core.fields as wagtail_fields

import wagtail.embeds.blocks
import wagtail.images.blocks


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("wagtailcore", "0041_group_collection_permissions_verbose_name_plural"),
    ]

    operations = [
        migrations.CreateModel(
            name="EditorGuide",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "information_text",
                    models.TextField(
                        blank=True,
                        help_text="Add a leading information paragraph explaining the guide",
                    ),
                ),
                (
                    "sections",
                    wagtail_fields.StreamField(
                        [
                            (
                                "heading",
                                wagtail_blocks.CharBlock(
                                    classname="full title",
                                    icon="title",
                                    template="wagtail_guide/streamfield/blocks/heading_block.html",
                                ),
                            ),
                            (
                                "paragraph",
                                wagtail_blocks.RichTextBlock(
                                    features=[
                                        "h2",
                                        "h3",
                                        "h4",
                                        "h5",
                                        "h6",
                                        "bold",
                                        "italic",
                                        "link",
                                        "ul",
                                        "ol",
                                        "hr",
                                    ]
                                ),
                            ),
                            (
                                "image",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "image",
                                            wagtail.images.blocks.ImageChooserBlock(),
                                        ),
                                        (
                                            "caption",
                                            wagtail_blocks.CharBlock(required=False),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "quote",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "quote",
                                            wagtail_blocks.CharBlock(classname="title"),
                                        ),
                                        (
                                            "attribution",
                                            wagtail_blocks.CharBlock(required=False),
                                        ),
                                    ]
                                ),
                            ),
                            (
                                "pull_quote",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "pull_quote",
                                            wagtail_blocks.CharBlock(classname="title"),
                                        )
                                    ]
                                ),
                            ),
                            (
                                "embed",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "title",
                                            wagtail_blocks.CharBlock(required=False),
                                        ),
                                        ("embed", wagtail.embeds.blocks.EmbedBlock()),
                                    ]
                                ),
                            ),
                            (
                                "video",
                                wagtail_blocks.StructBlock(
                                    [
                                        (
                                            "video",
                                            wagtail.embeds.blocks.EmbedBlock(
                                                label="Video URL", required=False
                                            ),
                                        )
                                    ]
                                ),
                            ),
                        ],
                        blank=True,
                    ),
                ),
                (
                    "site",
                    models.OneToOneField(
                        editable=False,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="wagtailcore.Site",
                    ),
                ),
            ],
            options={
                "verbose_name": "Manage Editor Guide",
            },
        ),
    ]
