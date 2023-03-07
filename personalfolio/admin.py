from django.contrib import admin
from . models import Profile, AboutUs, Experiance, Education, Skills, Services, Resume, Projects, HireMessage


class ProfileAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'name', 'house_name', 'city', 'district', 'state', 'country', 'pincode', 'dob', 'email', 'phone',
                    'profile_picture', 'gender', 'qualification', 'creator', 'updater', 'created_at', 'modified_at', 'is_deleted')
    list_display_links = ('creator', 'updater',)
    list_editable = ('profile_picture', 'gender',
                     'qualification', 'is_deleted')
    list_per_page = 5
    search_fields = ('name', 'auto_id', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(Profile, ProfileAdmin)


class AboutusAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'profile', 'website', 'profession', 'description',
                    'github', 'linkedin', 'skype', 'twitter', 'facebook', 'instagram', 'tryhackme',
                    'total_experiance', 'freelance', 'is_open_for_job', 'creator', 'updater', 'created_at', 'modified_at', 'is_deleted')
    list_display_links = ('creator', 'updater', 'profile',)
    list_editable = ('website', 'profession', 'github', 'linkedin', 'skype', 'twitter', 'facebook', 'instagram', 'tryhackme',
                     'total_experiance', 'freelance', 'is_open_for_job', 'is_deleted')
    list_per_page = 5
    search_fields = ('profile__name', 'auto_id', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(AboutUs, AboutusAdmin)


class ExperianceAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'profile', 'start', 'end', 'profession', 'description',
                    'reason_for_quite', 'creator', 'updater', 'created_at', 'modified_at', 'is_deleted')
    list_display_links = ('creator', 'updater', 'profile',)
    list_editable = ('start', 'end', 'profession', 'is_deleted')
    list_per_page = 5
    search_fields = ('start', 'profession', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(Experiance, ExperianceAdmin)


class EducationAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'profile', 'start', 'end', 'area_of_study', 'description',
                    'creator', 'updater', 'created_at', 'modified_at', 'is_deleted')
    list_display_links = ('creator', 'updater', 'profile',)
    list_editable = ('start', 'end', 'area_of_study', 'is_deleted')
    list_per_page = 5
    search_fields = ('start', 'area_of_study', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(Education, EducationAdmin)


class SkillsAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'profile', 'skill_name', 'skill_progress', 'skill_png', 'skill_font',
                    'is_visible', 'is_visible_icon', 'creator', 'updater', 'created_at', 'modified_at', 'is_deleted')
    list_display_links = ('creator', 'updater', 'profile',)
    list_editable = ('skill_name', 'skill_progress', 'is_deleted')
    list_per_page = 5
    search_fields = ('skill_name', 'skill_progress', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(Skills, SkillsAdmin)


class ServicesAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'profile', 'service_name', 'description', 'service_png', 'service_font',
                    'is_visible', 'is_visible_icon', 'creator', 'updater', 'created_at', 'modified_at', 'is_deleted')
    list_display_links = ('creator', 'updater', 'profile',)
    list_editable = ('service_name', 'is_deleted')
    list_per_page = 5
    search_fields = ('service_name', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(Services, ServicesAdmin)


class ResumeAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'profile', 'resume_profession_name', 'resume_year', 'resume_format', 'resume_link_from_driver',
                    'resume_file', 'cover_letter', 'creator', 'updater', 'created_at', 'modified_at', 'is_deleted')
    list_display_links = ('creator', 'updater', 'profile',)
    list_editable = ('resume_profession_name', 'resume_file', 'is_deleted')
    list_per_page = 5
    search_fields = ('resume_profession_name', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(Resume, ResumeAdmin)


class ProjectsAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'profile', 'project_name', 'description', 'project_image', 'github',
                    'online', 'creator', 'updater', 'created_at', 'modified_at', 'is_deleted')
    list_display_links = ('creator', 'updater', 'profile',)
    list_editable = ('project_name', 'project_image',
                     'github', 'online', 'is_deleted')
    list_per_page = 5
    search_fields = ('project_name', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(Projects, ProjectsAdmin)


class HireMessageAdmin(admin.ModelAdmin):
    # prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'auto_id', 'name', 'email', 'subject', 'message',
                    'sended_at', 'is_deleted')
    list_display_links = ('email',)
    # list_editable = ()
    list_per_page = 5
    search_fields = ('subject', 'is_deleted',)
    list_filter = ('is_deleted',)


admin.site.register(HireMessage, HireMessageAdmin)
