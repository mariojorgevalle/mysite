from polls.models import Poll
from django.contrib import admin

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
            (None, {'fields': ['pub_date']}),
            ('Date information', {'fields': ['question'], 'classes': ['collapse']}),
    ]

admin.site.register(Poll, PollAdmin)
