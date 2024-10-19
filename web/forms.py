from django import forms
from web.models import Questionnaire, Resume, Testimonial

from .models import CareerApplication, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"


class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        exclude = ("is_beginner", "is_regular", "is_partner", "created")


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = "__all__"


class CareerApplicationForm(forms.ModelForm):
    class Meta:
        model = CareerApplication
        exclude = ("career",)


class QuestionnaireForm(forms.ModelForm):
    class Meta:
        model = Questionnaire
        fields = "__all__"
