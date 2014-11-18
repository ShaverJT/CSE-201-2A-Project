from django.contrib import admin
from Applications.models import App, Review

# Register your models here.                                                                                                                                                         

class ReviewInline(admin.StackedInline):
    model = Review

class AppAdmin(admin.ModelAdmin):
    feildsets = [
        (None,               {'fields': ['app_name']}),
        (None,               {'fields': ['developers']}),
        ('Date Information', {'fields': ['pub_date']}),
        (None,               {'fields': ['description']}),
        ('Download Link',    {'fields': ['link']}),
        ('App Icon',         {'fields': ['pic']})
    ]
    inlines = [ReviewInline]


admin.site.register(App, AppAdmin)
