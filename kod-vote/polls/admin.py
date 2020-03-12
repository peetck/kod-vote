from django.contrib import admin
from .models import Poll, Poll_Choice, Poll_Vote
from django.contrib.auth.models import Permission
# Register your models here.

class ChoiceInline(admin.StackedInline): # inline
    model = Poll_Choice
    extra = 1

class PollAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'subject',
        'detail',
        'start_date',
        'end_date',
        'create_date',
        'is_active',
        'create_by'
    ]
    list_per_page = 10
    list_filter = ['create_by']
    search_fields = ['subject']

    inlines = [ChoiceInline]

class Poll_ChoiceAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'poll_id',
        'subject'
    ]

    search_fields = ['subject']

class Poll_VoteAdmin(admin.ModelAdmin):
    list_display = [
        'vote_by',
        'choice_id',
        'poll_id'
    ]

admin.site.register(Poll, PollAdmin)
admin.site.register(Poll_Choice, Poll_ChoiceAdmin)
admin.site.register(Poll_Vote, Poll_VoteAdmin)

admin.site.register(Permission)
