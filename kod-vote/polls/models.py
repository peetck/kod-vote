from django.utils import timezone

from django.contrib.auth.models import User
from django.db import models

# Create your models here.

class Poll(models.Model):
    subject = models.CharField(max_length=255, null=False)
    detail = models.TextField(null=False)
    picture = models.ImageField(default='poll/default.png', upload_to='poll/')
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField()
    password = models.CharField(max_length=255, default='')
    create_by = models.ForeignKey(User, on_delete=models.CASCADE)
    create_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.subject}'

    def is_available(self):
        if timezone.now() >= self.end_date:
            self.is_active = False
            self.save()
        return self.is_active

class Poll_Choice(models.Model):
    subject = models.CharField(max_length=255, null=False)
    image = models.ImageField(default='choice/default.png', upload_to='choice/')
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.subject}'

class Poll_Vote(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Poll_Choice, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)
