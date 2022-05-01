from django.contrib import admin
from .models import Quote

# Register your models here.
class QuoteAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'major', 'classification', 'email', 'username')
    list_filter = ('name', 'major')
    fieldsets = (
        (None, {
            "fields": (
                'name', 'bio', 'skills', 'languages', 'experience', 'picture'
            ),
        }),
        ('Contact Information', {
            'classes': ('collapse',),
            'fields': ('phone', 'email')
        }),
        ('Class Information', {
            'classes': ('collapse',),
            'fields': ('major', 'classification', 'graduation')
        }),
        ('Quote Admin', {
            'classes': ('collapse',),
            'fields': ('username',)
        }),
    )
    

admin.site.register(Quote, QuoteAdmin)