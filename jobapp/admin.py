from django.contrib import admin

from jobapp.models import JobPost,Location,Author,Skill

# Register your models here.
class JobPostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'description', 'salary', 'date', 'modified', 'jobtype', 'locations', 'authors', )
    list_filter = ('jobtype','authors',)
    raw_id_fields = ('locations','authors',)
    search_fields = ('title', 'slug', 'description', 'salary', 'date', 'modified', 'JOBTYPE_OPTION', 'jobtype', 'locations', 'author', 'skills', )
    filter_horizontal = ('skills',)
    prepopulated_fields = {'slug':('title',)}
admin.site.register(JobPost,JobPostAdmin)
class LocationAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'country', 'zip', )
    search_fields = ('city','state',)
admin.site.register(Location,LocationAdmin)

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name', 'company', 'designation', )
    list_filter = ('designation',)
    search_fields = ('name', 'company', 'designation', )
admin.site.register(Author,AuthorAdmin)
admin.site.register(Skill)