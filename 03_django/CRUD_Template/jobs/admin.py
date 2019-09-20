from django.contrib import admin
from .models import Jobs
# Register your models here.

class JobsAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'past_job',)

admin.site.register(Jobs, JobsAdmin)