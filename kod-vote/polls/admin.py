from django.contrib import admin
from .models import Poll, Poll_Choice, Poll_Vote
# Register your models here.

admin.site.register(Poll)
admin.site.register(Poll_Choice)
admin.site.register(Poll_Vote)
