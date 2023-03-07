import uuid
import datetime
from django.db import models
from versatileimagefield.fields import VersatileImageField
from django.utils.translation import gettext_lazy as _


YEAR_CHOICES = []
for r in range(1980, (datetime.datetime.now().year+1)):
    YEAR_CHOICES.append((r, r))


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    creator = models.ForeignKey("auth.User", blank=True,
                                related_name="creator_%(class)s_objects",
                                on_delete=models.CASCADE)
    updater = models.ForeignKey("auth.User", blank=True,
                                related_name="updator_%(class)s_objects",
                                on_delete=models.CASCADE)
    created_at = models.DateTimeField(db_index=True, auto_now_add=True)
    modified_at = models.DateTimeField(auto_now_add=True)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        abstract = True


class Profile(BaseModel):
    MALE = 1
    FEMALE = 2
    OTHER = 3

    GENDER_CHOICE = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Not Disclose'),
    )

    name = models.CharField(max_length=128)
    house_name = models.CharField(max_length=228)
    city = models.CharField(max_length=128)
    district = models.CharField(max_length=128)
    state = models.CharField(max_length=128)
    country = models.CharField(max_length=128)
    pincode = models.CharField(max_length=6)
    dob = models.DateField()
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    profile_picture = VersatileImageField('profile_picture',
                                          upload_to="profile_pictures/",
                                          blank=True, null=True)
    gender = models.PositiveSmallIntegerField(
        choices=GENDER_CHOICE, blank=True, null=True)
    qualification = models.CharField(max_length=128)

    class Meta:
        db_table = 'personalfolio_profile'
        verbose_name = _('profile')
        verbose_name_plural = _('profiles')
        ordering = ('-created_at', 'name')

    def __str__(self):
        return self.name


class AboutUs(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    website = models.CharField(max_length=128)
    profession = models.CharField(max_length=128)
    description = models.TextField(max_length=1500)
    github = models.CharField(max_length=228)
    linkedin = models.CharField(max_length=228)
    skype = models.CharField(max_length=228)
    twitter = models.CharField(max_length=228)
    facebook = models.CharField(max_length=228)
    instagram = models.CharField(max_length=228)
    tryhackme = models.CharField(max_length=228)
    total_experiance = models.PositiveIntegerField()
    freelance = models.BooleanField(default=False)
    is_open_for_job = models.BooleanField(default=True)

    class Meta:
        db_table = 'personalfolio_aboutus'
        verbose_name = _('aboutus')
        verbose_name_plural = _('aboutsus')
        ordering = ('-created_at', 'profile')

    def __str__(self):
        return self.profile.name


class Experiance(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start = models.IntegerField(
        _('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    end = models.IntegerField(
        _('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    profession = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)
    reason_for_quite = models.TextField(max_length=500, blank=True, null=True)

    class Meta:
        db_table = 'personalfolio_experiance'
        verbose_name = _('experiance')
        verbose_name_plural = _('experiances')
        ordering = ('-start', '-created_at', 'profile')

    def __str__(self):
        return self.profession


class Education(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    start = models.IntegerField(
        _('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    end = models.IntegerField(
        _('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    area_of_study = models.CharField(max_length=128)
    description = models.TextField(max_length=1000)

    class Meta:
        db_table = 'personalfolio_education'
        verbose_name = _('education')
        verbose_name_plural = _('educations')
        ordering = ('-start', '-created_at', 'profile')

    def __str__(self):
        return self.area_of_study


class Skills(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    skill_name = models.CharField(max_length=128)
    skill_progress = models.PositiveIntegerField()
    skill_png = VersatileImageField('skill_png',
                                    upload_to="skills/png/",
                                    blank=True, null=True)
    skill_font = models.CharField(max_length=128, blank=True, null=True)
    is_visible_icon = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)

    class Meta:
        db_table = 'personalfolio_skills'
        verbose_name = _('skill')
        verbose_name_plural = _('skills')
        ordering = ('skill_name', '-created_at', 'profile')

    def __str__(self):
        return self.skill_name


class Services(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    service_name = models.CharField(max_length=128)
    description = models.CharField(max_length=250)
    service_png = VersatileImageField('skill_png',
                                      upload_to="skills/png/",
                                      blank=True, null=True)
    service_font = models.CharField(max_length=128, blank=True, null=True)
    is_visible_icon = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=False)

    class Meta:
        db_table = 'personalfolio_services'
        verbose_name = _('service')
        verbose_name_plural = _('services')
        ordering = ('service_name', '-created_at', 'profile')

    def __str__(self):
        return self.service_name


class Resume(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    resume_profession_name = models.CharField(max_length=128)
    resume_year = models.IntegerField(
        _('year'), choices=YEAR_CHOICES, default=datetime.datetime.now().year)
    resume_format = models.CharField(max_length=128)
    resume_link_from_driver = models.CharField(
        max_length=228, blank=True, null=True)
    resume_file = models.FileField(upload_to="resume/files/",
                                   blank=True, null=True)
    cover_letter = models.FileField(upload_to="resume/files/",
                                    blank=True, null=True)

    class Meta:
        db_table = 'personalfolio_resume'
        verbose_name = _('resume')
        verbose_name_plural = _('resumes')
        ordering = ('resume_profession_name', '-created_at', 'profile')

    def __str__(self):
        return self.resume_profession_name


class Projects(BaseModel):
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    project_name = models.CharField(max_length=128)
    description = models.CharField(max_length=250)
    project_image = VersatileImageField('project_image',
                                        upload_to="projects/files/",
                                        blank=True, null=True)
    github = models.CharField(max_length=228, blank=True, null=True)
    online = models.CharField(max_length=228, blank=True, null=True)

    class Meta:
        db_table = 'personalfolio_projects'
        verbose_name = _('project')
        verbose_name_plural = _('projects')
        ordering = ('project_name', '-created_at', 'profile')

    def __str__(self):
        return self.project_name


class HireMessage(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    auto_id = models.PositiveIntegerField(db_index=True, unique=True)
    sended_at = models.DateTimeField(db_index=True, auto_now_add=True)
    name = models.CharField(max_length=128)
    email = models.EmailField()
    subject = models.CharField(max_length=128)
    company = models.CharField(max_length=128)
    message = models.TextField(max_length=2000)
    is_deleted = models.BooleanField(default=False)

    class Meta:
        db_table = 'personalfolio_hire_messages'
        verbose_name = _('hire_message')
        verbose_name_plural = _('hire_messages')
        ordering = ('name', '-sended_at', 'subject')

    def __str__(self):
        return self.email
