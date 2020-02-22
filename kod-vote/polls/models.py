from django.db import models
from accounts.models import User
# Create your models here.

class Poll(models.Model):
    subject = models.CharField(max_length=255)
    detail = models.TextField()
    #picture
    start_date = models.TimeField(auto_now=True)
    end_date = models.TimeField()
    password = models.CharField(max_length=255)
    create_by = models.CharField(max_length=255)
    create_date = models.TimeField(auto_now=True)

class Poll_Choice(models.Model):
    subject = models.CharField(max_length=255)
    #image
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)

class Poll_Vote(models.Model):
    poll_id = models.ForeignKey(Poll, on_delete=models.CASCADE)
    choice_id = models.ForeignKey(Poll_Choice, on_delete=models.CASCADE)
    vote_by = models.ForeignKey(User, on_delete=models.CASCADE)