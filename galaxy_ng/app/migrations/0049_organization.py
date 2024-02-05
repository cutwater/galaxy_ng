# Generated by Django 4.2.9 on 2024-02-05 16:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("galaxy", "0048_update_collection_remote_rhcertified_url"),
    ]

    operations = [
        migrations.CreateModel(
            name="Organization",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "created_on",
                    models.DateTimeField(
                        default=None,
                        editable=False,
                        help_text="The date/time this resource was created",
                    ),
                ),
                (
                    "modified_on",
                    models.DateTimeField(
                        default=None,
                        editable=False,
                        help_text="The date/time this resource was created",
                    ),
                ),
                (
                    "name",
                    models.CharField(
                        help_text="The name of this resource", max_length=512, unique=True
                    ),
                ),
                (
                    "description",
                    models.TextField(
                        blank=True, default="", help_text="The organization description."
                    ),
                ),
                (
                    "created_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        help_text="The user who created this resource",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="%(app_label)s_%(class)s_created+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "main_group",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="galaxy.group",
                    ),
                ),
                (
                    "modified_by",
                    models.ForeignKey(
                        default=None,
                        editable=False,
                        help_text="The user who last modified this resource",
                        null=True,
                        on_delete=django.db.models.deletion.DO_NOTHING,
                        related_name="%(app_label)s_%(class)s_modified+",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="OrganizationTeam",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True, primary_key=True, serialize=False, verbose_name="ID"
                    ),
                ),
                (
                    "organization",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="galaxy.organization",
                    ),
                ),
                (
                    "team",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="+",
                        to="galaxy.group",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="organization",
            name="teams",
            field=models.ManyToManyField(through="galaxy.OrganizationTeam", to="galaxy.group"),
        ),
        migrations.AddConstraint(
            model_name="organizationteam",
            constraint=models.UniqueConstraint(
                models.F("organization"), models.F("team"), name="uq_organization_team"
            ),
        ),
    ]
