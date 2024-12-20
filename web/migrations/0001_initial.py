# Generated by Django 4.2.9 on 2024-02-15 15:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="BeginnerLearn",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="begginer/learn"),
                ),
                ("video_url", models.URLField(blank=True, null=True)),
                ("content", models.TextField()),
                ("order", models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                "verbose_name": "Beginner Learn",
                "verbose_name_plural": "Beginner Learns",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Career",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("subtitle", models.CharField(max_length=100)),
                ("description", models.TextField()),
                ("responsibilities", models.TextField(blank=True, null=True)),
                ("skills", models.TextField(blank=True, null=True)),
                ("key_skills", models.TextField(blank=True, null=True)),
                ("experience", models.CharField(max_length=100)),
                ("qualification", models.CharField(max_length=100)),
                ("role", models.CharField(max_length=100)),
                ("location", models.CharField(max_length=100)),
                ("department", models.CharField(max_length=100)),
                ("employement_type", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Career",
                "verbose_name_plural": "Careers",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Contact",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("subject", models.CharField(max_length=100)),
                ("phone", models.CharField(max_length=20)),
                (
                    "email",
                    models.EmailField(max_length=254, verbose_name="Email Address"),
                ),
                ("message", models.TextField()),
            ],
            options={
                "verbose_name": "Contact",
                "verbose_name_plural": "Contacts",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="FAQ",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("photo", models.ImageField(blank=True, null=True, upload_to="update")),
                ("video_url", models.URLField(blank=True, null=True)),
                ("content", models.TextField()),
                (
                    "is_general",
                    models.BooleanField(default=False, verbose_name="Display in General FAQ"),
                ),
                (
                    "is_beginner",
                    models.BooleanField(default=False, verbose_name="Display in Beginner FAQ"),
                ),
            ],
            options={
                "verbose_name": "FAQ",
                "verbose_name_plural": "FAQs",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="LatestUpdate",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("slug", models.SlugField(unique=True)),
                ("photo", models.ImageField(upload_to="updates")),
                ("content", models.TextField()),
                ("video_url", models.URLField(blank=True, null=True)),
            ],
            options={
                "verbose_name": "Latest Update",
                "verbose_name_plural": "Latest Updates",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="PartnerGrowWithUs",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="regular/grow_with"),
                ),
                ("video_url", models.URLField(blank=True, null=True)),
                ("content", models.TextField()),
                ("order", models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                "verbose_name": "Grow with us",
                "verbose_name_plural": "Grow with us",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Questionnaire",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(max_length=128)),
                (
                    "description",
                    models.TextField(verbose_name="Do you have any Question to Ask ?"),
                ),
            ],
            options={
                "verbose_name": "Questionnaire",
                "verbose_name_plural": "Questionnaires",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="RegularUpskill",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "photo",
                    models.ImageField(blank=True, null=True, upload_to="regular/upskill"),
                ),
                ("video_url", models.URLField(blank=True, null=True)),
                ("content", models.TextField()),
                ("order", models.IntegerField(blank=True, null=True, unique=True)),
            ],
            options={
                "verbose_name": "Regular Upskill",
                "verbose_name_plural": "Regular Upskills",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="Resume",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("phone", models.CharField(max_length=128)),
                (
                    "resume",
                    models.FileField(blank=True, null=True, upload_to="testimonial/video"),
                ),
                (
                    "description",
                    models.TextField(verbose_name="What kind of Job you are looking for?"),
                ),
            ],
            options={
                "verbose_name": "Resume",
                "verbose_name_plural": "Resumes",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="Team",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("photo", models.ImageField(upload_to="images/testimonials")),
                ("designation", models.CharField(max_length=50)),
                ("is_active", models.BooleanField(default=True)),
                ("order", models.IntegerField(default=1)),
            ],
            options={
                "ordering": ("-order",),
            },
        ),
        migrations.CreateModel(
            name="Testimonial",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=128)),
                ("photo", models.ImageField(upload_to="images/testimonial")),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("content", models.TextField()),
                ("city", models.CharField(max_length=128)),
                ("created", models.DateTimeField(auto_now_add=True, db_index=True)),
                ("mt5_account", models.CharField(blank=True, max_length=20, null=True)),
                (
                    "video",
                    models.FileField(blank=True, null=True, upload_to="testimonial/video"),
                ),
                ("is_active", models.BooleanField(default=False)),
                (
                    "is_beginner",
                    models.BooleanField(default=False, verbose_name="Mark as Beginner Testimonial"),
                ),
                (
                    "is_regular",
                    models.BooleanField(default=False, verbose_name="Mark as Regular Client Testimonial"),
                ),
                (
                    "is_partner",
                    models.BooleanField(default=False, verbose_name="Mark as IB Testimonial"),
                ),
                (
                    "is_home_page",
                    models.BooleanField(default=False, verbose_name="Show in Homepage"),
                ),
            ],
            options={
                "verbose_name": "Testimonial",
                "verbose_name_plural": "Testimonials",
                "ordering": ("name",),
            },
        ),
        migrations.CreateModel(
            name="UpcomingEvent",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("description", models.TextField(blank=True, null=True)),
                ("photo", models.ImageField(upload_to="events")),
                ("date", models.CharField(max_length=100)),
                ("time", models.TimeField(blank=True, null=True)),
                ("venue", models.CharField(max_length=100)),
                ("is_active", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Upcoming Event",
                "verbose_name_plural": "Upcoming Events",
                "ordering": ("title",),
            },
        ),
        migrations.CreateModel(
            name="Update",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                ("photo", models.ImageField(blank=True, null=True, upload_to="update")),
                ("video_url", models.URLField(blank=True, null=True)),
                ("content", models.TextField()),
                ("is_regular", models.BooleanField(default=False)),
                ("is_partner", models.BooleanField(default=False)),
            ],
            options={
                "verbose_name": "Update",
                "verbose_name_plural": "Updates",
                "ordering": ("id",),
            },
        ),
        migrations.CreateModel(
            name="CareerApplication",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("email", models.EmailField(max_length=254)),
                ("phone", models.CharField(max_length=100)),
                ("resume", models.FileField(upload_to="career/resume")),
                (
                    "career",
                    models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to="web.career"),
                ),
            ],
            options={
                "verbose_name": "Career Application",
                "verbose_name_plural": "Career Applications",
                "ordering": ("name",),
            },
        ),
    ]
