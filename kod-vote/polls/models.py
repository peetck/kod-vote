from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Poll(models.Model):
    subject = models.CharField(max_length=50, blank=False, null=False)
    detail = models.TextField(blank=False, null=False)
    picture = models.ImageField(default='poll/poll_default.gif', upload_to='poll/')
    start_date = models.DateTimeField(default=timezone.now, blank=False, null=False)
    end_date = models.DateTimeField(blank=False, null=False)
    password = models.CharField(max_length=255, blank=False, null=False)
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.subject}'

    def is_available(self):
        if timezone.now() >= self.end_date or timezone.now() < self.start_date:
            self.is_active = False
            self.save()
        else:
            self.is_active = True
            self.save()
        return self.is_active

class Poll_Choice(models.Model):
    subject = models.CharField(max_length=40, blank=False, null=False)
    image = models.ImageField(default='choice/choice_default.gif', upload_to='choice/')
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject}'

class Poll_Vote(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Poll_Choice, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)
