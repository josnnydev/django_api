from django.contrib import admin
from .models import Project

# Register your models here.
admin.site.register(Project)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'technology', 'completed', 'create_at', 'updated_at')
    search_fields = ('title', 'description', 'technology')
    list_filter = ('completed',)
    readonly_fields = ('create_at', 'updated_at')

 





