from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from django_ckeditor_5.fields import CKEditor5Field


class Team(models.Model):
    name = models.CharField(max_length=50)
    photo = models.ImageField(upload_to="images/testimonials")
    designation = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    order = models.IntegerField(default=1)

    class Meta:
        ordering = ("-order",)

    def __str__(self):
        return str(self.name)


class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    email = models.EmailField(verbose_name=_("Email Address"))
    message = models.TextField()

    class Meta:
        verbose_name = _("Contact")
        verbose_name_plural = _("Contacts")
        ordering = ("id",)

    def __str__(self):
        return str(self.name)


class BeginnerLearn(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="begginer/learn", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField()
    order = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Beginner Learn")
        verbose_name_plural = _("Beginner Learns")
        ordering = ("id",)

    def __str__(self):
        return str(self.title)


class RegularUpskill(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="regular/upskill", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField()
    order = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Regular Upskill")
        verbose_name_plural = _("Regular Upskills")
        ordering = ("id",)

    def __str__(self):
        return str(self.title)


class Update(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="update", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField()
    is_regular = models.BooleanField(default=False)
    is_partner = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Update")
        verbose_name_plural = _("Updates")
        ordering = ("id",)

    def __str__(self):
        return str(self.title)


class FAQ(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="update", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField()
    is_general = models.BooleanField("Display in General FAQ", default=False)
    is_beginner = models.BooleanField("Display in Beginner FAQ", default=False)

    class Meta:
        verbose_name = _("FAQ")
        verbose_name_plural = _("FAQs")
        ordering = ("id",)

    def __str__(self):
        return str(self.title)


class Testimonial(models.Model):
    name = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="images/testimonial")
    email = models.EmailField(blank=True, null=True)
    content = models.TextField()
    city = models.CharField(max_length=128)
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    mt5_account = models.CharField(max_length=20, blank=True, null=True)
    video = models.FileField(upload_to="testimonial/video", blank=True, null=True)
    is_active = models.BooleanField(default=False)
    is_beginner = models.BooleanField("Mark as Beginner Testimonial", default=False)
    is_regular = models.BooleanField("Mark as Regular Client Testimonial", default=False)
    is_partner = models.BooleanField("Mark as IB Testimonial", default=False)
    is_home_page = models.BooleanField("Show in Homepage", default=False)

    class Meta:
        verbose_name = _("Testimonial")
        verbose_name_plural = _("Testimonials")
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class PartnerGrowWithUs(models.Model):
    title = models.CharField(max_length=100)
    photo = models.ImageField(upload_to="regular/grow_with", blank=True, null=True)
    video_url = models.URLField(blank=True, null=True)
    content = models.TextField()
    order = models.IntegerField(unique=True, blank=True, null=True)

    class Meta:
        verbose_name = _("Grow with us")
        verbose_name_plural = _("Grow with us")
        ordering = ("id",)

    def __str__(self):
        return str(self.title)


class Resume(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=128)
    resume = models.FileField(upload_to="testimonial/video", blank=True, null=True)
    description = models.TextField("What kind of Job you are looking for?")

    class Meta:
        verbose_name = _("Resume")
        verbose_name_plural = _("Resumes")
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class LatestUpdate(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    photo = models.ImageField(upload_to="updates")
    content = models.TextField()
    video_url = models.URLField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse("web:update_view", kwargs={"slug": self.slug})

    class Meta:
        verbose_name = _("Latest Update")
        verbose_name_plural = _("Latest Updates")
        ordering = ("title",)

    def __str__(self):
        return str(self.title)


class UpcomingEvent(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    photo = models.ImageField(upload_to="events")
    date = models.CharField(max_length=100)
    time = models.TimeField(blank=True, null=True)
    venue = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Upcoming Event")
        verbose_name_plural = _("Upcoming Events")
        ordering = ("title",)

    def __str__(self):
        return str(self.title)


class Career(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    description = models.TextField()
    responsibilities = models.TextField(blank=True, null=True)
    skills = models.TextField(blank=True, null=True)
    key_skills = models.TextField(blank=True, null=True)

    experience = models.CharField(max_length=100)
    qualification = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    employement_type = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)

    class Meta:
        verbose_name = _("Career")
        verbose_name_plural = _("Careers")
        ordering = ("title",)

    def __str__(self):
        return str(self.title)


class CareerApplication(models.Model):
    career = models.ForeignKey(Career, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    resume = models.FileField(upload_to="career/resume")

    class Meta:
        verbose_name = _("Career Application")
        verbose_name_plural = _("Career Applications")
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class Questionnaire(models.Model):
    name = models.CharField(max_length=128)
    email = models.EmailField(blank=True, null=True)
    phone = models.CharField(max_length=128)
    description = models.TextField(_("Do you have any Question to Ask ?"))

    class Meta:
        verbose_name = _("Questionnaire")
        verbose_name_plural = _("Questionnaires")
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class Author(models.Model):
    name = models.CharField(max_length=128)
    designation = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="author")
    description = models.TextField()

    class Meta:
        verbose_name = _("Author")
        verbose_name_plural = _("Authors")
        ordering = ("name",)

    def __str__(self):
        return str(self.name)


class Blog(models.Model):
    title = models.CharField(max_length=128)
    slug = models.SlugField(unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    photo = models.ImageField(upload_to="blog")
    content = CKEditor5Field(config_name="extends")
    created = models.DateTimeField(db_index=True, auto_now_add=True)
    is_active = models.BooleanField(default=False)
    is_home_page = models.BooleanField("Show in Homepage", default=False)

    class Meta:
        verbose_name = _("Blog")
        verbose_name_plural = _("Blogs")
        ordering = ("-created",)

    def get_absolute_url(self):
        return reverse("web:blog_view", kwargs={"slug": self.slug})

    def __str__(self):
        return str(self.title)


class Award(models.Model):
    image = models.ImageField(upload_to="award")
    title = models.CharField(max_length=225)
    award_name = models.CharField(max_length=225)
    is_home = models.BooleanField(default=False)
    
    class Meta:
        db_table = 'award'
        verbose_name = _('Award')
        verbose_name_plural = _('Awards')
    
    def __str__(self):
        return self.award_name
    

class Service(models.Model):
    service_name = models.CharField(max_length=180,blank=True,null=True)
    title = models.CharField(max_length=180)
    slug = models.SlugField()
    image = models.ImageField(upload_to="service_image")
    description = CKEditor5Field(config_name="extends")
    
    def get_absolute_url(self):
        return reverse("web:service_view", kwargs={"slug": self.slug})
    
    class Meta:
        db_table = 'service'
        verbose_name = 'Service'
        verbose_name_plural = 'Services'
    
    def __str__(self):
        return self.title