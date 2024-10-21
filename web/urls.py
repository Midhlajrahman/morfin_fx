from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("whatsapp/", views.whatsapp, name="whatsapp"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("awards/", views.awards, name="awards"),
    path("team/", views.team, name="team"),
    path("regulations/", views.regulations, name="regulations"),
    path("video_tutorials/", views.video_tutorials, name="video_tutorials"),
    path("latest_updates/", views.latest_updates, name="latest_updates"),
    path("update_view/<str:slug>/", views.update_view, name="update_view"),
    path("upcoming_events/", views.upcoming_events, name="upcoming_events"),
    path("market_updates/", views.market_updates, name="market_updates"),
    # beginner
    path("beginner/", views.beginner, name="beginner"),
    path("beginner/learn/", views.learn, name="learn"),
    path("beginner/stories/", views.beginner_stories, name="beginner_stories"),
    path("beginner/download_app/", views.download_app, name="download_app"),
    path(
        "regular/stories/share/",
        views.share_beginner_testimonial,
        name="share_beginner_testimonial",
    ),
    # regular
    path("regular/", views.regular, name="regular"),
    path("regular/upskill/", views.upskill, name="upskill"),
    path("regular/updates/", views.updates, name="updates"),
    path("regular/stories/", views.stories, name="stories"),
    path("regular/cip-calculator/", views.cip_calculator, name="cip_calculator"),
    path("regular/stories/share/", views.share_story, name="share_story"),
    # partner
    path("partner/", views.partner, name="partner"),
    path("partner/grow/", views.grow_with_us, name="grow_with_us"),
    path("partner/testimonial/", views.ib_testimonials, name="ib_testimonials"),
    path("partner/updates/", views.partner_updates, name="partner_updates"),
    path("partner/profit-calculator/", views.profit_calculator, name="profit_calculator"),
    path("partner/testimonial/share/", views.share_testimonial, name="share_testimonial"),
    # end
    path("plateform/MT5/", views.mt5, name="mt5"),
    path("plateform/MT5-web/", views.mt5_web, name="mt5_web"),
    path("manual/faq/", views.faq, name="faq"),
    path("manual/beginner_manual/", views.beginner_manual, name="beginner_manual"),
    path("manual/regular_manual/", views.regular_manual, name="regular_manual"),
    path("manual/partner_manual/", views.partner_manual, name="partner_manual"),
    path("career/vacancies/", views.vacancies, name="vacancies"),
    path(
        "career/vacancies/application/<str:pk>/",
        views.vacancies_application,
        name="vacancies_application",
    ),
    path("career/upload-CV/", views.upload_cv, name="upload_cv"),
    path(
        "withdrawal-refund-policy/",
        views.withdrawal_refund_policy,
        name="withdrawal_refund_policy",
    ),
    path("risk-warning/", views.risk_warning, name="risk_warning"),
    path("kyc-policy/", views.kyc_policy, name="kyc_policy"),
    path("client-agreement/", views.client_agreement, name="client_agreement"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-and-conditions/", views.terms_and_conditions, name="terms_and_conditions"),
    path(
        "google759971234a94a230.html",
        TemplateView.as_view(template_name="seo/google759971234a94a230.html"),
    ),
    path("blog/", views.blogs, name="blogs"),
    path("blog/<str:slug>/", views.blog_view, name="blog_view"),
    path("service/<slug:slug>/", views.service_view, name="service_view"),
]
