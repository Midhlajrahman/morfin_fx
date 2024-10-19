from django.contrib import admin
from django.contrib.auth.models import Group
from import_export.admin import ImportExportActionModelAdmin
from web.models import (
    FAQ,
    Author,
    BeginnerLearn,
    Blog,
    Career,
    CareerApplication,
    Contact,
    LatestUpdate,
    PartnerGrowWithUs,
    Questionnaire,
    RegularUpskill,
    Resume,
    Team,
    Testimonial,
    UpcomingEvent,
    Update,
    Award
)

admin.site.unregister(Group)


@admin.register(Contact)
class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "subject", "phone", "email")
    search_fields = ("name", "email")


@admin.register(Team)
class TeamAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "designation", "is_active", "order")
    search_fields = ("name", "designation")


@admin.register(BeginnerLearn)
class BeginnerLearnAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "order")


@admin.register(RegularUpskill)
class RegularUpskillAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "order")


@admin.register(PartnerGrowWithUs)
class PartnerGrowWithUsAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "order")


@admin.register(Update)
class UpdateAdmin(ImportExportActionModelAdmin):
    list_filter = ("is_regular", "is_partner")
    list_display = ("title", "is_regular", "is_partner")


@admin.register(FAQ)
class FAQAdmin(ImportExportActionModelAdmin):
    list_filter = ("is_general", "is_beginner")
    list_display = ("title", "is_general", "is_beginner")


@admin.register(Testimonial)
class TestimonialAdmin(ImportExportActionModelAdmin):
    list_filter = ("is_regular", "is_partner")
    list_display = ("name", "city", "email", "mt5_account", "is_regular", "is_partner")


@admin.register(Resume)
class ResumeAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "email", "phone")


@admin.register(LatestUpdate)
class LatestUpdateAdmin(ImportExportActionModelAdmin):
    list_display = ("title",)
    search_fields = ("title",)
    prepopulated_fields = {"slug": ("title",)}


@admin.register(UpcomingEvent)
class UpcomingEventAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "date", "time", "venue")


@admin.register(Career)
class CareerAdmin(ImportExportActionModelAdmin):
    list_display = (
        "title",
        "subtitle",
        "experience",
        "qualification",
        "location",
        "department",
    )
    search_fields = (
        "title",
        "subtitle",
        "experience",
        "qualification",
        "location",
        "department",
    )


@admin.register(CareerApplication)
class CareerApplicationAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "email", "phone", "resume")
    search_fields = ("name", "email", "phone", "resume")


@admin.register(Questionnaire)
class QuestionnaireAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "email", "phone")
    search_fields = ("name", "email", "phone")


@admin.register(Author)
class AuthorAdmin(ImportExportActionModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Blog)
class BlogAdmin(ImportExportActionModelAdmin):
    list_display = (
        "title",
        "author",
    )
    search_fields = (
        "title",
        "author",
    )
    prepopulated_fields = {"slug": ("title",)}
    autocomplete_fields = ("author",)


@admin.register(Award)
class AwardAdmin(ImportExportActionModelAdmin):
    list_display = ("award_name",)
    search_fields = ("award_name",)
    