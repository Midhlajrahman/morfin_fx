from django.http import JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.core.mail import send_mail
import urllib.parse

from web.models import FAQ, Team

from .forms import (
    CareerApplicationForm,
    ContactForm,
    QuestionnaireForm,
    ResumeForm,
    TestimonialForm,
)
from .models import (
    BeginnerLearn,
    Blog,
    Career,
    LatestUpdate,
    PartnerGrowWithUs,
    RegularUpskill,
    Testimonial,
    UpcomingEvent,
    Update,
    Award,
    Service
)


def whatsapp(request):
    whatsapp_link = "https://wa.me/+971586259739"
    return redirect(whatsapp_link)


def index(request):
    instances = Testimonial.objects.filter(is_home_page=True, is_active=True)
    blogs = Blog.objects.filter(is_home_page=True, is_active=True)
    awards = Award.objects.all()
    context = {"is_index": True, "instances": instances, "awards":awards, "blogs": blogs}
    return render(request, "web/index.html", context)


def awards(request):
    awards = Award.objects.all()
    context = {"is_awards": True, "awards":awards}
    return render(request, "web/awards.html", context)


def team(request):
    context = {"is_team": True, "teams": Team.objects.filter(is_active=True)}
    return render(request, "web/team.html", context)


def regulations(request):
    context = {"is_regulations": True}
    return render(request, "web/regulations.html", context)


def video_tutorials(request):
    context = {"is_video_tutorials": True}
    return render(request, "web/video_tutorials.html", context)


def latest_updates(request):
    instances = LatestUpdate.objects.all().order_by("-id")
    context = {"is_latest_updates": True, "instances": instances}
    return render(request, "web/latest_updates.html", context)


def update_view(request, slug):
    instance = LatestUpdate.objects.get(slug=slug)
    context = {"is_latest_updates": True, "instance": instance}
    return render(request, "web/update_view.html", context)


def upcoming_events(request):
    instances = UpcomingEvent.objects.filter(is_active=True).order_by("-id")
    context = {"is_upcoming_events": True, "instances": instances}
    return render(request, "web/upcoming_events.html", context)


def market_updates(request):
    context = {"is_market_updates": True}
    return render(request, "web/market_updates.html", context)


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            
            subject = "Contact Enquiry Information"
            message = (
                f'Name: {data.name} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Subject: {data.subject}\n'
                f'Message: {data.message}\n'
            )
            from_email = "support@morfinfx.com"
            recipient_list = ["pradeep@morfin.world",]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            whatsapp_message = (
                f'Name: {data.name} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Subject: {data.subject}\n'
                f'Message: {data.message}\n'
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+971586259739"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            
            return redirect(whatsapp_url)
        else:
            error_messages = {field: form.errors[field][0] for field in form.errors}
            print("Form Validation Error:", error_messages)  
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
            return JsonResponse(response_data)
    else:
        form = ContactForm()
        context = {
            "is_contact": True,
            "title": "Contact",
            "form": form,
            "redirect": True,
            "is_need_popup_box": True,
        }
    return render(request, "web/contact.html", context)


def about(request):
    context = {"is_about": True, "teams": Team.objects.filter(is_active=True)}
    return render(request, "web/about.html", context)


def beginner(request):
    context = {"is_beginner": True}
    return render(request, "web/beginner.html", context)


def learn(request):
    instances = BeginnerLearn.objects.all().order_by("order")
    context = {"instances": instances}
    return render(request, "web/beginner/learn.html", context)


def beginner_stories(request):
    instances = Testimonial.objects.filter(is_beginner=True, is_active=True)
    context = {"is_beginner_stories": True, "instances": instances}
    return render(request, "web/beginner/beginner_stories.html", context)


def download_app(request):
    context = {"is_download_app": True}
    return render(request, "web/beginner/download_app.html", context)


def regular(request):
    context = {"is_regular": True}
    return render(request, "web/regular.html", context)


def upskill(request):
    instances = RegularUpskill.objects.all().order_by("order")
    context = {"instances": instances}
    return render(request, "web/regular/upskill.html", context)


def updates(request):
    instances = Update.objects.filter(is_regular=True)
    context = {"instances": instances}
    return render(request, "web/regular/updates.html", context)


def stories(request):
    instances = Testimonial.objects.filter(is_regular=True, is_active=True)
    context = {"instances": instances}
    return render(request, "web/regular/stories.html", context)


def cip_calculator(request):
    context = {}
    return render(request, "web/regular/cip_calculator.html", context)


def partner(request):
    context = {"is_partner": True}
    return render(request, "web/partner.html", context)


def grow_with_us(request):
    instances = PartnerGrowWithUs.objects.all().order_by("order")
    context = {"instances": instances}
    return render(request, "web/partner/grow_with_us.html", context)


def ib_testimonials(request):
    instances = Testimonial.objects.filter(is_partner=True, is_active=True)
    context = {"instances": instances}
    return render(request, "web/partner/ib_testimonials.html", context)


def partner_updates(request):
    instances = Update.objects.filter(is_partner=True)
    context = {"instances": instances}
    return render(request, "web/partner/updates.html", context)


def profit_calculator(request):
    context = {}
    return render(request, "web/partner/profit_calculator.html", context)


def share_story(request):
    form = TestimonialForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.is_regular = True
            data.save()
            response_data = {
                "status": True,
                "title": "Successfully Submited",
                "message": "Your Story has been sent successfully.",
            }
        else:
            response_data = {
                "status": False,
                "message": str(form.errors),
                "title": "Form validation error",
            }
        return JsonResponse(response_data)
    context = {
        "title": "Share Story",
        "form": form,
        "redirect": True,
        "is_need_popup_box": True,
    }
    return render(request, "web/regular/share_story.html", context)


def share_testimonial(request):
    form = TestimonialForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.is_partner = True
            data.save()
            response_data = {
                "status": True,
                "title": "Successfully Submited",
                "message": "Your Testimonial has been sent successfully.",
            }
        else:
            response_data = {
                "status": False,
                "message": str(form.errors),
                "title": "Form validation error",
            }
        return JsonResponse(response_data)
    context = {
        "title": "Share Story",
        "form": form,
        "redirect": True,
        "is_need_popup_box": True,
    }
    return render(request, "web/partner/share_story.html", context)


def share_beginner_testimonial(request):
    form = TestimonialForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.is_beginner = True
            data.save()
            response_data = {
                "status": True,
                "title": "Successfully Submited",
                "message": "Your Testimonial has been sent successfully.",
            }
        else:
            response_data = {
                "status": False,
                "message": str(form.errors),
                "title": "Form validation error",
            }
        return JsonResponse(response_data)
    context = {
        "title": "Share Story",
        "form": form,
        "redirect": True,
        "is_need_popup_box": True,
    }
    return render(request, "web/beginner/share_story.html", context)


def mt5(request):
    context = {"is_mt5": True, "is_plateform": True}
    return render(request, "web/plateform/mt5.html", context)


def mt5_web(request):
    context = {"is_mt5_web": True, "is_plateform": True}
    return render(request, "web/plateform/mt5_web.html", context)


def faq(request):
    instances = FAQ.objects.filter(is_general=True)
    form = QuestionnaireForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            response_data = {
                "status": True,
                "title": "Your Question Recieved",
                "message": "We have recieved your question and we will get in touch with you soon",
            }
        else:
            response_data = {
                "status": False,
                "message": str(form.errors),
                "title": "Form validation error",
            }
        return JsonResponse(response_data)
    context = {"is_faq": True, "is_manual": True, "instances": instances, "form": form}
    return render(request, "web/manual/faq.html", context)


def beginner_manual(request):
    context = {"beginner_manual": True, "is_manual": True}
    return render(request, "web/manual/beginner_manual.html", context)


def regular_manual(request):
    context = {"regular_manual": True, "is_manual": True}
    return render(request, "web/manual/regular_manual.html", context)


def partner_manual(request):
    context = {"partner_manual": True, "is_manual": True}
    return render(request, "web/manual/partner_manual.html", context)


def vacancies(request):
    instances = Career.objects.filter(is_active=True)
    context = {"is_vacancies": True, "is_career": True, "instances": instances}
    return render(request, "web/career/vacancies.html", context)


def vacancies_application(request, pk):
    instance = get_object_or_404(Career, pk=pk)
    form = CareerApplicationForm(request.POST or None, request.FILES or None)
    if request.method == "POST":
        if form.is_valid():
            data = form.save(commit=False)
            data.career = instance
            data.save()
            response_data = {
                "status": True,
                "title": "Successfully Submited",
                "message": "Your Application has been sent successfully.",
            }
        else:
            response_data = {
                "status": False,
                "message": str(form.errors),
                "title": "Form validation error",
            }
        return JsonResponse(response_data)
    context = {
        "is_vacancies_application": True,
        "is_career": True,
        "instance": instance,
        "form": form,
    }
    return render(request, "web/career/vacancies_application.html", context)


def upload_cv(request):
    if request.method == "POST":
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.save(commit=False)
            data.save()
            
            subject = "Career Enquiry Information"
            message = (
                f'Name: {data.name} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Resume: https://morfin.geany.website/{data.resume.url}\n'
                f'Description: {data.description}\n'
            )
            from_email = "support@morfinfx.com"
            recipient_list = ["pradeep@morfin.world",]
            send_mail(subject, message, from_email, recipient_list, fail_silently=False)
            
            whatsapp_message = (
                f'Name: {data.name} \n'
                f'Email: {data.email}\n'
                f'Phone: {data.phone}\n'
                f'Resume: https://morfin.geany.website/{data.resume.url}\n'
                f'Description: {data.description}\n'
            )
            whatsapp_api_url = "https://api.whatsapp.com/send"
            phone_number = "+971586259739"
            encoded_message = urllib.parse.quote(whatsapp_message)
            whatsapp_url = f"{whatsapp_api_url}?phone={phone_number}&text={encoded_message}"
            
            return redirect(whatsapp_url)
        else:
            error_messages = {field: form.errors[field][0] for field in form.errors}
            print("Form Validation Error:", error_messages)  
            response_data = {
                "status": "false",
                "title": "Form Validation Error",
                "message": error_messages,
            }
            return JsonResponse(response_data)
    else:
        form = ResumeForm()
        context = {"is_upload_cv": True, "is_career": True, "form": form}
    return render(request, "web/career/upload_cv.html", context)


def withdrawal_refund_policy(request):
    return render(request, "web/withdrawal_refund_policy.html")


def risk_warning(request):
    return render(request, "web/risk_warning.html")


def kyc_policy(request):
    return render(request, "web/kyc_policy.html")


def client_agreement(request):
    return render(request, "web/client_agreement.html")


def privacy_policy(request):
    return render(request, "web/privacy_policy.html")


def terms_and_conditions(request):
    return render(request, "web/terms_and_conditions.html")


def blogs(request):
    blogs = Blog.objects.filter(is_active=True)
    context = {"blogs": blogs}
    return render(request, "web/blogs.html", context)


def blog_view(request, slug):
    blog = get_object_or_404(Blog, slug=slug)
    return render(request, "web/blog_view.html", {"blog": blog})


def service_view(request, slug):
    service = get_object_or_404(Service, slug=slug)
    context = {"service": service}
    return render(request, "web/service_view.html", context)